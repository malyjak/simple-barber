from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import schemas, database, crud


app = FastAPI()

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
    return {"message": "User deleted successfully"}
