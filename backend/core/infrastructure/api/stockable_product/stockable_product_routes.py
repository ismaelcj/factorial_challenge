from fastapi import APIRouter, HTTPException

from backend.core.application.stockable_product.create.create_stockable_product_command import \
    CreateStockableProductCommand
from backend.core.infrastructure.api.stockable_product.stockable_product_requests import CreateStockableProductRequest
from backend.shared.infrastructure.dependencies import CommandBusInstance

router = APIRouter(prefix="/product/stockable", tags=["stockable_product"])

@router.put("/new")
async def create_stockable_product(
        request: CreateStockableProductRequest,
        command_bus: CommandBusInstance
) -> None:
    try:
        command = CreateStockableProductCommand(
            product_id=request.id,
            name=request.name,
            category=request.category,
            price=request.price,
            stock_units=request.stock_units
        )
        command_bus.dispatch(command)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
