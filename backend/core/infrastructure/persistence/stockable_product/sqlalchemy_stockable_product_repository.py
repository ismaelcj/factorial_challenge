from sqlalchemy.orm import Session

from backend.core.domain.stockable_product.stockable_product_repository import StockableProductRepository
from backend.core.infrastructure.persistence.sqlalchemy_product_repository import SqlalchemyProductRepository
from backend.core.infrastructure.persistence.stockable_product.stockable_product_model import StockableProductModel


class SqlalchemyStockableProductRepository(StockableProductRepository):
    def __init__(self, db_session: Session):
        self._db_session = db_session
        self.product_repository = SqlalchemyProductRepository(db_session)
    
    def update_stock(self, product_id: str, quantity: int) -> None:
        stockable_model = self._db_session.query(StockableProductModel).filter(
            StockableProductModel.product_id == product_id
        ).first()
        
        if not stockable_model:
            raise ValueError(f"Stockable product with ID {product_id} not found")
            
        stockable_model.stock_units = quantity
        self._db_session.flush()
