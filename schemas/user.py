from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    role : Optional[str] = "user"

class UserCreate(UserBase):
    # email: Optional[EmailStr] =None
    password: str = Field(..., min_length=6, max_length=30)

class UserUpdate(UserBase):
    email: Optional[EmailStr] =None
    password: Optional[str] = Field(None, min_length=6, max_length=30)
    role: Optional[str] = None

class UserRead(UserBase):
    id: int
    email: EmailStr
    role: str

    class Config:
        orm_mode = True
