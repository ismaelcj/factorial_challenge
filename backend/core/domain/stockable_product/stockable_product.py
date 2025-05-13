from typing import Optional

from backend.core.domain.category import Category
from backend.core.domain.pricing_context import PricingContext
from backend.core.domain.product import Product, ProductType
from backend.shared.domain.value_objects.custom_uuid import Uuid


class StockableProduct(Product):
    def __init__(
            self,
            product_id: Uuid,
            name: str,
            category: Category,
            stock_units: int,
            price: float
    ):
        super().__init__(product_id, name, category, ProductType.STOCKABLE)
        self._stock_units = stock_units
        self._price = price

    @classmethod
    def create(
            cls,
            product_id: str,
            name: str,
            category: str,
            price: float,
            stock_units: int = 0
    ) -> 'StockableProduct':
        return cls(
            Uuid(product_id),
            name,
            Category(category),
            stock_units,
            price
        )

    def available_units(self) -> int:
        return self._stock_units

    def increase_stock(self, units: int) -> None:
        assert units > 0
        self._stock_units += units

    def decrease_stock(self, units: int) -> None:
        assert units > 0
        assert self._stock_units >= units
        self._stock_units -= units

    def get_price(self, context: Optional[PricingContext] = None) -> float:
        return self._price

    def to_primitives(self) -> dict:
        return {
            'id': self.id.value,
            'name': self.name,
            'category': self.category.value,
            'stock_units': self._stock_units,
            'price': self._price
        }
