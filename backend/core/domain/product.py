from abc import abstractmethod

from backend.shared.domain.aggregate_root import AggregateRoot
from backend.shared.domain.value_objects.custom_uuid import Uuid
from backend.core.domain.category import Category


class Product(AggregateRoot):
    def __init__(self, product_id: Uuid, name: str, category: Category):
        super().__init__(product_id)
        self._name = name
        self._category = category

    @abstractmethod
    def get_price(self) -> float:
        pass

    @property
    def category(self) -> Category:
        return self._category

    def __repr__(self):
        return f"Product[{self._name} category={self._category}]"
