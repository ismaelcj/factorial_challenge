from typing import List

from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.core.domain.product_type import ProductType
from backend.core.infrastructure.persistence.product_model import ProductModel
# from backend.core.infrastructure.persistence.service_product.price_rule_model import PriceRuleModel
from backend.shared.infrastructure.persistence.database import SQLBase


class ServiceProductModel(ProductModel):
    __tablename__ = "service_product"

    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"), primary_key=True)
    price_rules: Mapped[List["PriceRuleModel"]] = relationship(
        back_populates="service",
        cascade="all, delete-orphan",
    )

    __mapper_args__ = {
        "polymorphic_identity": ProductType.SERVICE,
    }


class PriceRuleModel(SQLBase):
    __tablename__ = "price_rule"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    recipient_product_id: Mapped[str] = mapped_column(ForeignKey("product.id"))
    price: Mapped[float] = mapped_column(Float, default=0.0)
    service_id: Mapped[str] = mapped_column(ForeignKey("service_product.product_id"))
    service: Mapped["ServiceProductModel"] = relationship(
        back_populates="price_rules",
        foreign_keys=[service_id]
    )
