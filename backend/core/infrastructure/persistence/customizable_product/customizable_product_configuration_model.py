from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.core.infrastructure.persistence.customizable_product.product_option_model import ProductOptionModel
from backend.shared.infrastructure.persistence.database import SQLBase


class CustomizableProductConfigurationModel(SQLBase):
    __tablename__ = "customizable_product_configuration"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)
    options: Mapped[List[ProductOptionModel]] = relationship(
        back_populates="configuration",
        cascade="all, delete-orphan",
    )
    product_id = mapped_column(ForeignKey("customizable_product.product_id"))
    product = relationship("CustomizableProductModel", back_populates="configuration")
