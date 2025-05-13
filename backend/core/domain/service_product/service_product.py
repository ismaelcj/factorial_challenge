from typing import Optional

from backend.core.domain.category import Category
from backend.core.domain.pricing_context import PricingContext
from backend.core.domain.product import Product
from backend.core.domain.product_type import ProductType
from backend.core.domain.service_product.null_price_rule import NullPriceRule
from backend.core.domain.service_product.price_rule import PriceRule
from backend.shared.domain.value_objects.custom_uuid import Uuid


class ServiceProduct(Product):
    def __init__(self, service_id: Uuid, name: str, category: Category):
        super().__init__(service_id, name, category, ProductType.SERVICE)
        self._price_rules = list[PriceRule]()

    @classmethod
    def create(cls, product_id: str, name: str, category: Category) -> 'ServiceProduct':
        return cls(
            Uuid(product_id),
            name,
            category
        )

    def add_price_rule(self, product: Product, price: float) -> None:
        assert self.get_price_rule(product).is_null(), "Price rule already exists"
        price_rule = PriceRule(product, price)
        self._price_rules.append(price_rule)

    def get_price_rule(self, product: Product) -> PriceRule:
        for price_rule in self._price_rules:
            if price_rule.is_applicable(product):
                return price_rule
        return NullPriceRule()

    def get_price(self, context: Optional[PricingContext] = None) -> float:
        assert context.applicable_products is not None, \
            "A list of applicable products is required for service price calculation"
        price = 0.0
        for product in context.applicable_products:
            price_rule = self.get_price_rule(product)
            price += price_rule.apply(product)
        return price

    def to_primitives(self) -> dict:
        return {
            'product_id': self.id.value,
            'name': self.name,
            'category': self.category.value,
            'price_rules': [rule.to_primitives() for rule in self._price_rules]
        }
