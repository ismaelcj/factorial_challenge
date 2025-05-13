from pydantic import BaseModel


class CreateStockableProductRequest(BaseModel):
    id: str
    name: str
    category: str
    price: float
    stock_units: int
