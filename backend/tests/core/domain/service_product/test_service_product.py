import pytest

from backend.core.domain.pricing_context import PricingContext
from backend.tests.core.domain.service_product.service_product_mother import ServiceProductMother
from backend.tests.core.domain.stockable_product.stockable_product_mother import StockableProductMother

def test_add_price_rule():
    service = ServiceProductMother.create()
    product = StockableProductMother.create()
    price = 100
    
    service.add_price_rule(product, price)

    context = PricingContext(applicable_products=[product])
    assert service.get_price(context) == price

def test_cannot_add_duplicate_price_rule():
    service = ServiceProductMother.create()
    product = StockableProductMother.create()
    price = 100
    
    service.add_price_rule(product, price)
    
    with pytest.raises(AssertionError):
        service.add_price_rule(product, 200)

def test_get_correct_price_rule():
    service = ServiceProductMother.create()
    product1 = StockableProductMother.create()
    product2 = StockableProductMother.create()
    price_product1 = 100

    service.add_price_rule(product1, price_product1)

    context = PricingContext(applicable_products=[
        product1,
        product2
    ])
    assert service.get_price(context) == price_product1
