from backend.core.domain.product_compatibility.product_compatibility_service import ProductCompatibilityService
from backend.shared.domain.value_objects.custom_uuid import Uuid
from backend.tests.core.domain.product_compatibility.product_incompatibility_mother import ProductIncompatibilityMother
from backend.tests.core.domain.stockable_product.stockable_product_mother import StockableProductMother


class TestProductCompatibility:
    
    def test_are_incompatible_same_order(self):
        incompatibility = ProductIncompatibilityMother.create()
        product_a_id = incompatibility.product_a_id
        product_b_id = incompatibility.product_b_id

        result = incompatibility.are_incompatible(product_a_id, product_b_id)

        assert result is True
    
    def test_are_incompatible_reverse_order(self):
        incompatibility = ProductIncompatibilityMother.create()
        product_a_id = incompatibility.product_a_id
        product_b_id = incompatibility.product_b_id

        result = incompatibility.are_incompatible(product_b_id, product_a_id)

        assert result is True
    
    def test_are_compatible(self):
        incompatibility = ProductIncompatibilityMother.create()
        other_product_id = Uuid.generate()

        result = incompatibility.are_incompatible(incompatibility.product_a_id, other_product_id)

        assert result is False
    
    def test_product_is_incompatible_with_other_product(self):
        product_a = StockableProductMother.create(name="ProductA")
        product_b = StockableProductMother.create(name="ProductB")
        incompatibility = ProductIncompatibilityMother.create_for_products(
            product_a.id, product_b.id, "Incompatible products"
        )
        incompatibilities = [incompatibility]

        result = product_a.is_incompatible_with(product_b, incompatibilities)

        assert result is True
    
    def test_product_is_compatible_with_other_product(self):
        product_a = StockableProductMother.create(name="ProductA")
        product_b = StockableProductMother.create(name="ProductB")
        product_c = StockableProductMother.create(name="ProductC")
        incompatibility = ProductIncompatibilityMother.create_for_products(
            product_a.id, product_c.id, "Incompatible products"
        )
        incompatibilities = [incompatibility]

        result = product_a.is_incompatible_with(product_b, incompatibilities)

        assert result is False
    
    def test_compatibility_service_validates_compatible_products(self):
        product = StockableProductMother.create(name="TestProduct")
        other_products = [StockableProductMother.create(name="OtherProduct") for _ in range(3)]
        incompatibilities = []

        result = ProductCompatibilityService.validate_compatibility(
            product, other_products, incompatibilities
        )

        assert result.is_valid
    
    def test_compatibility_service_invalidates_incompatible_products(self):
        product = StockableProductMother.create(name="TestProduct")
        incompatible_product = StockableProductMother.create(name="IncompatibleProduct")
        other_products = [
            StockableProductMother.create(name="Product1"),
            incompatible_product,
            StockableProductMother.create(name="Product2")
        ]
        incompatibility = ProductIncompatibilityMother.create_for_products(
            product.id, incompatible_product.id, "Incompatible products"
        )
        incompatibilities = [incompatibility]

        result = ProductCompatibilityService.validate_compatibility(
            product, other_products, incompatibilities
        )

        assert not result.is_valid
        assert f"Cannot add {product.name} as it is incompatible with {incompatible_product.name}" in result.message
