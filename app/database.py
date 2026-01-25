from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite database file (test.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# For SQLite, need this argument
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Import models after Base is created to avoid circular imports
from app.models.user import User

# Dependency to get DB session
