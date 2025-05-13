from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.core.infrastructure.persistence.customizable_product.customizable_product_configuration_model import \
    CustomizableProductConfigurationModel
from backend.core.infrastructure.persistence.customizable_product.product_option_value_model import \
    ProductOptionValueModel
from backend.core.infrastructure.persistence.product_model import ProductModel


class CustomizableProductModel(ProductModel):
    __tablename__ = "customizable_product"

    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"), primary_key=True)
    configuration: Mapped[CustomizableProductConfigurationModel] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
    )
    selected_values: Mapped[List[ProductOptionValueModel]] = relationship(
        back_populates="customizable_product",
        cascade="all, delete-orphan",
    )

    __mapper_args__ = {
        "polymorphic_identity": "customizable",
    }
