from typing import List, Dict
from promotion import Promotion
from sku import SKU
import math


class Cart:
    def __init__(self, skus: List[SKU], promotions: Dict[str, List[Promotion]]):
        self.skus_qty = dict()
        for sku in skus:
            self.skus_qty[sku] = self.skus_qty.get(sku, 0) + 1
        self.promotions = promotions

    def get_price(self) -> float:

        total_price = 0
        for sku, qty in self.skus_qty.items():
            sku_proms = self.promotions.get(sku.barcode)
            price = sku.price * qty
            if not sku_proms:
                total_price += price
                continue
            min_price = math.inf
            for prom in sku_proms:
                if qty >= prom.qty:
                    min_price = min(price - prom.discount, min_price)
            total_price += min_price
        return total_price
