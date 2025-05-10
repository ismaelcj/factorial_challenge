import uuid

from core.domain.stockable_product.stockable_product import StockableProduct


class StockableProductMother:
    @staticmethod
    def create(
        product_id: str = uuid.uuid4().hex,
        name: str = "Test Product",
        price: float = 100.0,
    ) -> StockableProduct:
        return StockableProduct.create(product_id, name, price)

    @staticmethod
    def create_with_stock(
        stock: int = 10,
        product_id: str = uuid.uuid4().hex,
        name: str = "Test Product With Stock",
        price: float = 100.0,
    ) -> StockableProduct:
        product = StockableProduct.create(product_id, name, price)
        product.increase_stock(stock)
        return product
