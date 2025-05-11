from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from backend.core.domain.product import Product


class PricingContext:
    def __init__(self, applicable_products: List["Product"] = None, **kwargs) -> None:
        self.applicable_products = applicable_products
        self.additional_params = kwargs
