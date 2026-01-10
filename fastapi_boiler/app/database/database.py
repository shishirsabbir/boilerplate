# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.database.base import Base


# defining engine
db_url = f"sqlite:///{settings.database_url}"
engine = create_engine(
    db_url,
    connect_args={"check_same_thread": False} if db_url.startswith("sqlite") else {},
)


# creating session using sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# create all tables
Base.metadata.create_all(bind=engine)


# get db function
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
