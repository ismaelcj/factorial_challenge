from backend.core.domain.stockable_product.stockable_product_repository import StockableProductRepository
from backend.shared.domain.cqrs.command_handler import CommandHandler


class UpdateStockableProduct(CommandHandler):
    def __init__(self, repository: StockableProductRepository):
        self._repository = repository

    def handle(self, command):
        pass
    #     product = self._repository.find_by_id(command.product_id)
    #     product.update(
    #         name=command.name,
    #         category=command.category,
    #         stock_units=command.stock_units,
    #         price=command.price
    #     )
    #     self._repository.save(product)
