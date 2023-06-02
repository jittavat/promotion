from cart import Cart
from promotion import Promotion
from sku import SKU
from typing import Tuple


def main(barcodes: Tuple[str]):
    # initial SKUs & promotion
    all_skus = dict()
    all_promotions = dict()
    for i in range(2000):
        barcode = str(i).zfill(5)
        price = i + 10
        sku = SKU(barcode, str(i), price)
        all_skus[barcode] = sku

        promo_code = str(i).zfill(10)
        all_promotions[barcode] = [Promotion(f"{promo_code}{i}", i, barcode, round(price * 0.1 * i)) for i in
                                   range(1, 6)]

    skus = [all_skus[barcode] for barcode in barcodes]
    cart = Cart(skus, all_promotions)
    print(cart.get_price())


if __name__ == '__main__':
    # main(('00001', '00005', '00005', '00002', '00003', '00500'))
    main(('00500', '00500', '00500', '00500', '00500'))
