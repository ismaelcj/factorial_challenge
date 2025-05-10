from backend.core.domain.category import Category
from backend.core.domain.product import Product
from backend.core.domain.service_product.null_price_rule import NullPriceRule
from backend.core.domain.service_product.price_rule import PriceRule
from backend.shared.domain.value_objects.custom_uuid import Uuid


class ServiceProduct(Product):
    def __init__(self, service_id: Uuid, name: str, category: Category):
        super().__init__(service_id, name, category)
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

    def get_price(self, applied_to: Product = None) -> float:
        price_rule = self.get_price_rule(applied_to)
        return price_rule.apply(applied_to)
