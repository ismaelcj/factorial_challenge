from abc import abstractmethod

from backend.shared.domain.aggregate_root import AggregateRoot
from backend.shared.domain.value_objects.custom_uuid import Uuid


class Product(AggregateRoot):
    def __init__(self, product_id: Uuid, name: str):
        super().__init__(product_id)
        self._name = name

    @abstractmethod
    def get_price(self) -> float:
        pass
