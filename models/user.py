from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    # hashed_password = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")  # 예: "admin", "user"
