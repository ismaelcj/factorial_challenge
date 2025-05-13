from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.infrastructure.persistence.product_model import ProductModel


class StockableProductModel(ProductModel):
    __tablename__ = "stockable_product"

    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"), primary_key=True)
    stock_units: Mapped[int] = mapped_column(default=0)
    price: Mapped[float] = mapped_column(Float, default=0.0)

    __mapper_args__ = {
        "polymorphic_identity": "stockable",
    }
