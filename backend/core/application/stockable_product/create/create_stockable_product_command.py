from dataclasses import dataclass

from backend.shared.domain.cqrs.command import Command


@dataclass(frozen=True)
class CreateStockableProductCommand(Command):
    product_id: str
    name: str
    category: str
    stock_units: int
    price: float
