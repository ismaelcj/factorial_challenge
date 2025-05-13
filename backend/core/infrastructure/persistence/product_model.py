from sqlalchemy.orm import Mapped, mapped_column

from backend.shared.infrastructure.persistence.database import SQLBase


class ProductModel(SQLBase):
    __tablename__ = "product"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column()
    category: Mapped[str] = mapped_column()
    type: Mapped[str] = mapped_column()
    
    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": None
    }
