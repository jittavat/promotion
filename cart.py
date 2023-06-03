from typing import List, Dict
from promotion import Promotion
from sku import SKU
import numpy as np


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

            p = [0]
            wt = [0]
            for prom in sku_proms:
                for _ in range(int(qty / prom.qty) + 1):
                    p.append(prom.discount)
                    wt.append(prom.qty)
            total_price += price - self.knapsack_dynamic_programming(qty, np.array(p), np.array(wt, dtype=int))
        return total_price

    @staticmethod
    def knapsack_dynamic_programming(m: int, p: np.ndarray, wt: np.ndarray) -> float:
        n = len(p) - 1
        k = np.zeros((n + 1, m + 1))

        for i in range(1, n + 1):
            for w in range(1, m + 1):
                if wt[i] <= w:
                    k[i][w] = max(p[i] + k[i - 1][w - wt[i]], k[i - 1][w])
                else:
                    k[i][w] = k[i - 1][w]
        return k[n, m]
