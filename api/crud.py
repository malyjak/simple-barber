from sqlalchemy.orm import Session
from . import models, schemas


def get_slots(db: Session, skip: int = 0, limit: int = 100) -> list[models.Slot]:
    return db.query(models.Slot).offset(skip).limit(limit).all()

def get_slot(db: Session, slot_id: int) -> models.Slot:
    return db.query(models.Slot).filter(models.Slot.id == slot_id).first()

def create_slot(db: Session, slot: schemas.SlotCreate) -> models.Slot:
    db_slot = models.Slot(**slot.model_dump())
    db.add(db_slot)
    db.commit()
    db.refresh(db_slot)

    return db_slot

def update_slot(db: Session, slot_id: int, slot_update:schemas.SlotUpdate) -> models.Slot:
    db_slot = get_slot(db, slot_id=slot_id)
    if db_slot is not None:
        db_slot.date = slot_update.date
        db_slot.occupied = slot_update.occupied
        db.commit()

    return db_slot

def delete_slot(db: Session, slot_id: int) -> models.Slot:
    db_slot = get_slot(db, slot_id=slot_id)
    if db_slot is not None:
        db.delete(db_slot)
        db.commit()

    return db_slot
