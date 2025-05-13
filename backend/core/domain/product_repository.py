from abc import ABC, abstractmethod
from typing import List

from backend.core.domain.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> None:
        pass

    @abstractmethod
    def find_by_id(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def exists(self, product_id) -> bool:
        pass
    
    @abstractmethod
    def find_all(self) -> List[Product]:
        pass

    # @abstractmethod
    # def find_stockable_by_id(self, product_id: str) -> StockableProduct:
    #     """Find stockable product by ID or raise exception if not found or wrong type"""
    #     pass
    #
    # @abstractmethod
    # def find_service_by_id(self, product_id: str) -> ServiceProduct:
    #     """Find service product by ID or raise exception if not found or wrong type"""
    #     pass
    #
    # @abstractmethod
    # def find_customizable_by_id(self, product_id: str) -> CustomizableProduct:
    #     """Find customizable product by ID or raise exception if not found or wrong type"""
    #     pass
