from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.controllers.user_controller import create_user, get_users, get_user
from sqlalchemy.ext.declarative import declarative_base
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{id}", response_model=UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return get_user(db, id)