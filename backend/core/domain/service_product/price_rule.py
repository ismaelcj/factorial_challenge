from backend.core.domain.product import Product


class PriceRule:
    def __init__(self, recipient_product: Product, price: float):
        self._recipient_product = recipient_product
        self._price = price

    def is_applicable(self, product: Product) -> bool:
        return self._recipient_product == product

    def apply(self, product: Product) -> float:
        assert self.is_applicable(product)
        return self._price

    def is_null(self):
        return False

    def to_primitives(self) -> dict:
        return {
            'recipient_product_id': self._recipient_product.id.value,
            'price': self._price
        }
