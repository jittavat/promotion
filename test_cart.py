import pytest
from promotion import Promotion
from sku import SKU
from cart import Cart


@pytest.fixture
def skus():
    return [
        SKU("00001", "1", 100),
        SKU("00002", "2", 200)
    ]


def test_simple_case(skus):
    promotions = {'00001': [Promotion('001', 1, '00001', 50)]}
    cart = Cart(skus, promotions)
    assert cart.get_price() == 250


def test_multiple_item_matches_single_promo(skus):
    skus.append(SKU("00001", "1", 100))
    promotions = {'00001': [Promotion('001', 1, '00001', 50), Promotion('001', 2, '00001', 110)]}
    cart = Cart(skus, promotions)
    assert cart.get_price() == 290


def test_multiple_item_matches_multiple_promo(skus):
    skus.append(SKU("00001", "1", 100))
    promotions = {'00001': [Promotion('001', 1, '00001', 50), Promotion('001', 2, '00001', 99),
                            Promotion('001', 3, '00001', 500)]}
    cart = Cart(skus, promotions)
    assert cart.get_price() == 300


def test_multiple_item_sku_matches_multiple_promo(skus):
    skus.append(SKU("00001", "1", 100))
    promotions = {'00001': [Promotion('001', 1, '00001', 50), Promotion('002', 2, '00001', 99),
                            Promotion('003', 3, '00001', 500)],
                  '00002': [Promotion('004', 1, '00002', 1), Promotion('005', 2, '00002', 100),
                            Promotion('006', 3, '00002', 500)]}
    cart = Cart(skus, promotions)
    assert cart.get_price() == 299
