from typing import Annotated

from _pytest.main import Session
from fastapi import Depends

from backend.core.application.stockable_product.create.create_stockable_product import CreateStockableProduct
from backend.core.application.stockable_product.create.create_stockable_product_command import \
    CreateStockableProductCommand
from backend.core.infrastructure.persistence.sqlalchemy_product_repository import SqlalchemyProductRepository
from backend.core.infrastructure.persistence.stockable_product.sqlalchemy_stockable_product_repository import \
    SqlalchemyStockableProductRepository
from backend.shared.infrastructure.cqrs.memory_command_bus import MemoryCommandBus
from backend.shared.infrastructure.persistence.database import get_db


command_bus = MemoryCommandBus()

def initial_setup(db: Session = next(get_db())):
    stockable_product_repository = SqlalchemyProductRepository(db_session=db)

    command_bus.register(
        CreateStockableProductCommand,
        CreateStockableProduct(
            repository=stockable_product_repository
        )
    )

def get_command_bus():
    return command_bus

CommandBusInstance = Annotated[MemoryCommandBus, Depends(get_command_bus)]
