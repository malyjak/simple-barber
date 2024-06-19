from datetime import timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import schemas, database, crud, auth


app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Administration
# @app.get("/users/me/", response_model=schemas.User)
# def get_users_me(current_user: schemas.User = Depends(auth.get_current_user)):
#     return current_user

# @app.get("/users/{username}", response_model=schemas.User)
# def get_user(username: str, db: Session = Depends(database.get_db)):
#     db_user = crud.get_service(db, username=username)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user=user)

@app.post("/token/", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    db_user = crud.authenticate_user(db, username=form_data.username, password=form_data.password)
    if db_user is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"},)
    access_token = auth.create_access_token(
        data={"sub": db_user.username}
    )

    return {"access_token": access_token, "token_type": "bearer"}


# Services.
@app.get("/services/", response_model=list[schemas.Service])
def get_services(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    db_services = crud.get_services(db, skip=skip, limit=limit)
    return db_services

@app.get("/services/{service_id}", response_model=schemas.Service)
def get_service(service_id: int, db: Session = Depends(database.get_db)):
    db_service = crud.get_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@app.post("/services/", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(database.get_db)):
    return crud.create_service(db, service=service)

@app.put("/services/{service_id}", response_model=schemas.Service)
def update_service(service_id: int, service_update: schemas.ServiceUpdate, db: Session = Depends(database.get_db)):
    db_service = crud.update_service(db, service_id=service_id, service_update=service_update)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@app.delete("/services/{service_id}")
def delete_service(service_id: int, db: Session = Depends(database.get_db)):
    db_service = crud.delete_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}




@app.get("/admin/slots/", response_model=list[schemas.Slot])
def get_slots(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    db_slots = crud.get_slots(db, skip=skip, limit=limit)
    return db_slots

@app.get("/admin/slots/{slot_id}", response_model=schemas.Slot)
def get_slot(slot_id: int, db: Session = Depends(database.get_db)):
    db_slot = crud.get_slot(db, slot_id=slot_id)
    if db_slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")
    return db_slot

@app.post("/admin/slots/", response_model=schemas.Slot)
def create_slot(slot: schemas.SlotCreate, db: Session = Depends(database.get_db)):
    return crud.create_slot(db, slot=slot)

@app.put("/admin/slots/{slot_id}", response_model=schemas.Slot)
def update_slot(slot_id: int, slot_update: schemas.SlotUpdate, db: Session = Depends(database.get_db)):
    db_slot = crud.update_slot(db, slot_id=slot_id, slot_update=slot_update)
    if db_slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")
    return db_slot

@app.delete("/admin/slots/{slot_id}")
def delete_slot(slot_id: int, db: Session = Depends(database.get_db)):
    db_slot = crud.delete_slot(db, slot_id=slot_id)
    if db_slot is None:
        raise HTTPException(status_code=404, detail="Slot not found")
    return {"message": "Slot deleted successfully"}
