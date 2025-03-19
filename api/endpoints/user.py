from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.deps import get_db
import crud
from schemas.user import UserCreate, UserRead, UserUpdate
from models.user import User
from crud.user import create_user, get_users

router = APIRouter()
@router.get("/", response_model=List[UserRead])
# def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
def read_users(db: Session = Depends(get_db)):
    # users = get_users(db, skip=skip, limit=limit)
    users = crud.user.get_users(db)
    return users

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session=Depends(get_db)):
    db_user = crud.user.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user

@router.post("/", response_model=UserRead, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # 이미 존재하는 유저인지 확인
    # existing_user = db.query(...).filter(...).first()
    existing_user =crud.user.get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already registered")
    new_user = crud.user.create_user(db, user_in)
    return new_user

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id : int, user_in: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.user.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = crud.user.update_user(db, db_user, user_in)
    return  updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session= Depends(get_db)):
    db_user = crud.user.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.user.delete_user(db, db_user)
    return  {"detail" : "User deleted"}

# @router.get("/users")
# def read_users():
#     return [{"id": 1, "name": "bonnie"}, {"id": 2, "name": "Bob"}]
#
# @router.post("/users")
# def create_user(name: str):
#     return {"id": 3, "name": name}
