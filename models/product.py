from sqlalchemy import Column, Integer, String, Numeric
from db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, default=0)
