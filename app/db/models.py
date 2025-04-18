from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
