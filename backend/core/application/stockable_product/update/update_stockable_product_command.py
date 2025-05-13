from dataclasses import dataclass

from backend.shared.domain.cqrs.command import Command

@dataclass(frozen=True)
class UpdateStockableProductCommand(Command):
    name: str
    category: str
    stock_units: int
    price: float
