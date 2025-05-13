from abc import ABC, abstractmethod

class StockableProductRepository(ABC):
    @abstractmethod
    def update_stock(self, product_id: str, new_stock: int) -> None:
        pass
