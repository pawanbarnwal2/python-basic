from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.exceptions import UserNotFound, InvalidUserData, DuplicateEmail

def create_user(db: Session, user: UserCreate):
    # Check for duplicate email
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise DuplicateEmail()
    
    new_user = User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):

	return db.query(User).all()

def get_user(db: Session, user_id: int):
	user = db.query(User).filter(User.id == user_id).first()
	if not user:
		raise UserNotFound()
	return user

	
        
