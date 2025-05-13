from backend.core.domain.category import Category
from backend.core.domain.stockable_product.stockable_product import StockableProduct
from backend.shared.domain.value_objects.custom_uuid import Uuid


class StockableProductMother:
    @staticmethod
    def create(
        product_id: str = Uuid.generate().value,
        name: str = "Test Product",
        category: Category = Category.FRAME,
        price: float = 100.0,
    ) -> StockableProduct:
        return StockableProduct.create(product_id, name, category.value, price)

    @staticmethod
    def create_with_stock(
        stock: int = 10,
        product_id: str = Uuid.generate().value,
        name: str = "Test Product With Stock",
        category: Category = Category.FRAME,
        price: float = 100.0,
    ) -> StockableProduct:
        product = StockableProduct.create(product_id, name, category.value, price)
        product.increase_stock(stock)
        return product
