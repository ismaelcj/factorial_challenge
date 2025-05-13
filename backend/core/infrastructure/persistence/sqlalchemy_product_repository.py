from typing import List, Optional, Type

from sqlalchemy import exists
from sqlalchemy.orm import Session

from backend.core.domain.product import Product
from backend.core.domain.product_repository import ProductRepository
from backend.core.domain.stockable_product.stockable_product import StockableProduct
from backend.core.domain.service_product.service_product import ServiceProduct
from backend.core.domain.customizable_product.customizable_product import CustomizableProduct

from backend.core.infrastructure.persistence.product_model import ProductModel
from backend.core.infrastructure.persistence.stockable_product.stockable_product_model import StockableProductModel
from backend.core.infrastructure.persistence.service_product.service_product_model import ServiceProductModel
from backend.core.infrastructure.persistence.customizable_product.customizable_product_model import CustomizableProductModel


class SqlalchemyProductRepository(ProductRepository):
    def __init__(self, db_session: Session):
        self._db_session = db_session

    def save(self, product: Product) -> None:
        model = self._to_model(product)
        self._db_session.add(model)
        self._db_session.commit()

    def exists(self, product_id) -> bool:
        exists_query = self._db_session.query(
            exists().where(ProductModel.id == product_id)
        ).scalar()
        return exists_query

    def find_by_id(self, product_id: str) -> Optional[Product]:
        model = self._db_session.query(ProductModel).filter(ProductModel.id == product_id).one()
        if not model:
            return None
        return self._to_domain(model)

    def find_all(self) -> List[Product]:
        pass
    
    def find_by_category(self, category: str) -> List[Product]:
        pass

    def delete(self, product_id: str) -> None:
        model = self._db_session.query(ProductModel).filter(ProductModel.id == product_id).first()
        if model:
            self._db_session.delete(model)
            self._db_session.commit()

    def update(self, product: Product) -> None:
        existing = self._db_session.query(ProductModel).filter(ProductModel.id == product.id).first()
        if not existing:
            raise ValueError(f"Product with ID {product.id} not found")
            
        model = self._to_model(product)
        self._db_session.merge(model)
        self._db_session.commit()

    def _to_model(self, product: Product) -> ProductModel:
        from pprint import pprint
        pprint("*** In _to_model")
        """Convert a domain product to a SQLAlchemy model."""
        if isinstance(product, StockableProduct):
            return StockableProductModel(**product.to_primitives())
        elif isinstance(product, ServiceProduct):
            return ServiceProductModel(product.to_primitives())
        elif isinstance(product, CustomizableProduct):
            return self._customizable_to_model(product)
        else:
            raise ValueError(f"Unknown product type: {type(product)}")

    def _customizable_to_model(self, product: CustomizableProduct) -> CustomizableProductModel:
        pass

    def _to_domain(self, model: Type[ProductModel]) -> Product:
        pass