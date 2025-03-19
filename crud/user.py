from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from db.session import SessionLocal

def create_user(db: Session, user_in: UserCreate) -> User:
    db_user = User(
        email=user_in.email,
        # hashed_password=user_in.hashed_password,
        password=user_in.password,
        role=user_in.role or "user"
        # 기타 필드
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, db_user: User, user_in: UserUpdate) -> User:
    if user_in.email:
        db_user.email = user_in.email
    if user_in.password:
        # db_user.hashed_password = user_in.password  # 해싱 가정
        db_user.password = user_in.password  # 해싱 가정
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user: User) -> None:
    db.delete(db_user)
    db.commit()
