import pytest

from backend.core.domain.category import Category
from backend.core.domain.customizable_product.customizable_product import CustomizableProduct
from backend.core.domain.product import Product

from backend.tests.core.domain.customizable_product.customizable_product_mother import CustomizableProductMother
from backend.tests.core.domain.service_product.service_product_mother import ServiceProductMother
from backend.tests.core.domain.stockable_product.stockable_product_mother import StockableProductMother


def test_create_customizable_product():
    product = CustomizableProductMother.create()
    assert isinstance(product, CustomizableProduct)
    assert isinstance(product, Product)

def test_add_option_to_customizable_product():
    product = CustomizableProductMother.create()
    product.add_option("Frame", Category.FRAME, True)
    product.add_option("Wheels", Category.WHEELS, False)

def test_cannot_add_duplicate_category_option():
    product = CustomizableProductMother.create()
    product.add_option("Frame", Category.FRAME, True)
    
    with pytest.raises(AssertionError, match="Category already exists in this configuration"):
        product.add_option("Other Frame", Category.FRAME, True)

def test_add_product_option_value():
    customizable_product = CustomizableProductMother.create_with_options()
    options = customizable_product.options
    option_category = options[0].category

    product = StockableProductMother.create_with_stock(category=option_category)
    customizable_product.add_product_option_value(options[0], product)

    assert len(customizable_product._selected_values) == 1

def test_cannot_add_duplicate_option_value():
    customizable_product = CustomizableProductMother.create_with_options()
    options = customizable_product.options
    option_category = options[0].category

    product1 = StockableProductMother.create_with_stock(name="Product1", category=option_category)
    product2 = StockableProductMother.create_with_stock(name="Product2", category=option_category)

    customizable_product.add_product_option_value(options[0], product1)
    
    with pytest.raises(AssertionError, match="Option already exists in this product"):
        customizable_product.add_product_option_value(options[0], product2)

def test_get_price_with_valid_options():
    customizable_product = CustomizableProductMother.create_with_options()
    options = customizable_product.options
    option1 = options[0]
    option2 = options[1]

    product1 = StockableProductMother.create_with_stock(name="Product1", category=option1.category)
    product2 = StockableProductMother.create_with_stock(name="Product2", category=option2.category)

    customizable_product.add_product_option_value(option1, product1)
    customizable_product.add_product_option_value(option2, product2)
    
    assert customizable_product.get_price() == product1.get_price() + product2.get_price()

def test_get_price_with_service_product_option():
    frame_product = StockableProductMother.create_with_stock(
        name="Frame", category=Category.FRAME, price=200.0)
    wheels_product = StockableProductMother.create_with_stock(
        name="Wheels", category=Category.WHEELS, price=100.0)

    service = ServiceProductMother.create()
    service_price_for_frame = 20.0
    service.add_price_rule(frame_product, service_price_for_frame)
    service_price_for_wheels = 10.0
    service.add_price_rule(wheels_product, service_price_for_wheels)

    customizable_product = CustomizableProductMother.create()
    customizable_product.add_option("Frame", Category.FRAME, True)
    customizable_product.add_option("Wheels", Category.WHEELS, True)
    customizable_product.add_option("Frame Finish", Category.FRAME_FINISH, False)

    options = customizable_product.options
    customizable_product.add_product_option_value(options[0], frame_product)
    customizable_product.add_product_option_value(options[1], wheels_product)
    customizable_product.add_product_option_value(options[2], service)

    expected_service_price = service_price_for_frame + service_price_for_wheels
    expected_customizable_product_price = frame_product.get_price() + \
                                          wheels_product.get_price() + \
                                          expected_service_price

    assert customizable_product.get_price() == expected_customizable_product_price
