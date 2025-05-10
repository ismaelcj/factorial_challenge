from backend.core.domain.product import Product
from backend.core.domain.service_product.price_rule import PriceRule


class NullPriceRule(PriceRule):
    def __init__(self):
        pass

    def is_applicable(self, product: Product) -> bool:
        return False

    def apply(self, product: Product) -> float:
        return 0

    def __eq__(self, other):
        if not isinstance(other, NullPriceRule):
            return False
        return True

    def is_null(self):
        return True
