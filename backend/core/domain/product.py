from abc import abstractmethod
from typing import Optional, List

from backend.core.domain.category import Category
from backend.core.domain.pricing_context import PricingContext
from backend.core.domain.product_compatibility.product_incompatibility import ProductIncompatibility
from backend.core.domain.product_type import ProductType
from backend.shared.domain.aggregate_root import AggregateRoot
from backend.shared.domain.value_objects.custom_uuid import Uuid


class Product(AggregateRoot):
    def __init__(self, product_id: Uuid, name: str, category: Category, product_type: ProductType):
        super().__init__(product_id)
        self._name = name
        self._category = category
        self._product_type = product_type

    @abstractmethod
    def get_price(self, context: Optional[PricingContext] = None) -> float:
        pass

    def is_incompatible_with(self, other_product: 'Product', incompatibilities: List['ProductIncompatibility']) -> bool:
        for incompatibility in incompatibilities:
            if incompatibility.are_incompatible(self.id, other_product.id):
                return True
        return False

    # def get_incompatible_products(self, products: List['Product'], incompatibilities: List['ProductIncompatibility']) -> List['Product']:
    #     return [product for product in products if self.is_incompatible_with(product, incompatibilities)]

    @property
    def category(self) -> Category:
        return self._category

    @property
    def name(self) -> str:
        return self._name

    @property
    def product_type(self) -> ProductType:
        return self._product_type

    def __repr__(self):
        return f"Product[{self._name} category={self._category}, type={self._product_type}]"
