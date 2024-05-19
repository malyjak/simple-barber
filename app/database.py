from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base


DB_USER = "simple-barber-user"
DB_PASS = "simple-barber-pass"
DB_NAME = "simple-barber-db"
DB_ADDR = "localhost"
DB_PORT = 5432
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
