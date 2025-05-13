from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from backend.core.infrastructure.persistence.customizable_product.product_option_model import ProductOptionModel
from backend.core.infrastructure.persistence.product_model import ProductModel
from backend.shared.infrastructure.persistence.database import SQLBase


class ProductOptionValueModel(SQLBase):
    __tablename__ = "product_option_value"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)

    option_id: Mapped[str] = mapped_column(ForeignKey("product_option.id"))
    option: Mapped[ProductOptionModel] = relationship()

    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"))
    product: Mapped[ProductModel] = relationship()

    customizable_product_id = mapped_column(ForeignKey("customizable_product.product_id"))
    customizable_product = relationship(
        "CustomizableProductModel",
        back_populates="selected_values",
        foreign_keys=[customizable_product_id]
    )
