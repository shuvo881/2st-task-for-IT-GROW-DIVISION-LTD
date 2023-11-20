from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends

DATABASE_URL = "postgresql+psycopg2://agricultural_ai_doctor_user:B0Ok0TtZo3It7XNnJpNKqmA6p0zQDmjX@dpg-cjsbit4tjf3s73b309vg-a.oregon-postgres.render.com/agricultural_ai_doctor"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

