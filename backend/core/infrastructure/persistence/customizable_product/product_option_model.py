from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.shared.infrastructure.persistence.database import SQLBase


class ProductOptionModel(SQLBase):
    __tablename__ = "product_option"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    required: Mapped[bool] = mapped_column(default=False, nullable=False)

    configuration_id = mapped_column(ForeignKey("customizable_product_configuration.id"))
    configuration = relationship(
        "CustomizableProductConfigurationModel",
        back_populates="options"
    )
