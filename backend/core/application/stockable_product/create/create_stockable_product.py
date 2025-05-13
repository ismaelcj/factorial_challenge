from backend.core.application.stockable_product.create.create_stockable_product_command import \
    CreateStockableProductCommand
from backend.core.domain.product_service import ProductService
from backend.core.domain.stockable_product.stockable_product import StockableProduct
from backend.core.domain.stockable_product.stockable_product_repository import StockableProductRepository
from backend.shared.domain.cqrs.command_handler import CommandHandler



class CreateStockableProduct(CommandHandler):
    def __init__(self, repository: StockableProductRepository):
        self._repository = repository

    def handle(self, command: CreateStockableProductCommand) -> None:
        from pprint import pprint
        pprint(f"CreateStockableProduct.handle")
        ProductService.ensure_product_not_exists(command.product_id, self._repository)
        product = StockableProduct.create(
            product_id=command.product_id,
            name=command.name,
            category=command.category,
            stock_units=command.stock_units,
            price=command.price
        )
        self._repository.save(product)
        pprint(f"CreateStockableProduct.handle END")
        # TODO: Publish domain events if needed
