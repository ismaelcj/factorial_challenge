import pytest

from backend.tests.core.domain.stockable_product.stockable_product_mother import StockableProductMother

def test_increase_stock():
    product = StockableProductMother.create()
    initial_stock = product.available_units()

    stock_to_increase = 5
    product.increase_stock(stock_to_increase)
    
    assert product.available_units() == initial_stock + stock_to_increase

def test_decrease_stock():
    initial_stock = 10
    product = StockableProductMother.create_with_stock(stock=initial_stock)

    stock_to_decrease = 3
    product.decrease_stock(stock_to_decrease)
    
    assert product.available_units() == initial_stock - stock_to_decrease

def test_cannot_decrease_below_zero():
    initial_stock = 5
    product = StockableProductMother.create_with_stock(stock=initial_stock)

    stock_to_decrease = initial_stock + 1
    with pytest.raises(AssertionError):
        product.decrease_stock(stock_to_decrease)
