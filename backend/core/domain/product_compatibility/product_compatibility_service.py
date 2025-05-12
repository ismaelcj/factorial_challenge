from typing import List

from backend.core.domain.product import Product
from backend.core.domain.product_compatibility.product_incompatibility import ProductIncompatibility
from backend.shared.domain.value_objects.validation_result import ValidationResult


class ProductCompatibilityService:

    @staticmethod
    def validate_compatibility(
        product: Product, 
        products_to_check: List[Product],
        incompatibilities: List[ProductIncompatibility]
    ) -> ValidationResult:
        for other_product in products_to_check:
            if product.is_incompatible_with(other_product, incompatibilities):
                return ValidationResult.invalid(
                    f"Cannot add {product.name} as it is incompatible with {other_product.name}")
        return ValidationResult.valid()
