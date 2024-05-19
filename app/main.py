from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from .database import get_db
from .models import User
from .schema import UserCreate, UserUpdate


app = FastAPI()


@app.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/users/{user_email}")
def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)

    try:
        db.commit()
        return {"message": "User created successfully"}
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            raise HTTPException(status_code=400, detail="Email already in use")
        else:
            raise HTTPException(status_code=400, detail="Bad request")

@app.put("/users/{user_email}")
def update_user_by_email(user_email: str, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.password = user.password
    db.commit()
    return {"message": "User updated successfully"}

@app.delete("/users/{user_email}")
def delete_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user_email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
