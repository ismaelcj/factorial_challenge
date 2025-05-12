from abc import abstractmethod
from typing import Optional, List

from backend.core.domain.pricing_context import PricingContext
from backend.shared.domain.aggregate_root import AggregateRoot
from backend.shared.domain.value_objects.custom_uuid import Uuid
from backend.core.domain.category import Category
from backend.core.domain.product_compatibility.product_incompatibility import ProductIncompatibility


class Product(AggregateRoot):
    def __init__(self, product_id: Uuid, name: str, category: Category):
        super().__init__(product_id)
        self._name = name
        self._category = category

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

    def __repr__(self):
        return f"Product[{self._name} category={self._category}]"
