from backend.core.domain.product_repository import ProductRepository


class ProductService:
    @staticmethod
    def ensure_product_not_exists(product_id: str, repository: ProductRepository) -> None:
        if repository.exists(product_id):
            raise ValueError(f"Product with ID {product_id} already exists.")
