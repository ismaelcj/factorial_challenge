from typing import Optional

from backend.core.domain.customizable_product.product_option import ProductOption
from backend.core.domain.pricing_context import PricingContext
from backend.core.domain.product import Product
from backend.shared.domain.value_objects.custom_uuid import Uuid


class ProductOptionValue:
    def __init__(self, option_value_id: Uuid, option: ProductOption, product: Product):
        self._id = option_value_id
        self._option = option
        self._product = product

    @classmethod
    def create(
            cls,
            option_value_id: str,
            option: ProductOption,
            product: Product
    ) -> 'ProductOptionValue':
        assert cls.is_product_valid_for_option(product, option), \
            "Product category does not match option category"
        return cls(
            Uuid(option_value_id),
            option,
            product
        )

    @classmethod
    def is_product_valid_for_option(cls, product: Product, option: ProductOption) -> bool:
        return product.category == option.category

    def get_price(self, context: Optional[PricingContext] = None) -> float:
        return self._product.get_price(context)

    @property
    def option_id(self) -> Uuid:
        return self._option.id

    @property
    def product(self) -> Product:
        return self._product

    @property
    def id(self):
        return self._id

    def __repr__(self) -> str:
        return f"ProductOptionValue[{self._option} product={self._product}]"
