from sqlalchemy.orm import Session
from . import models, schemas, auth


# Auth operations.
def get_user(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
        hashed_password = auth.get_password_hash(user.password)
        db_user = models.User(username=user.username,
                              hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

def authenticate_user(db: Session, username: str, password: str):
    db_user = get_user(db, username)
    if db_user is not None:
        if auth.verify_password(password, db_user.hashed_password):
            return db_user

    return None


# Service operations.
def get_services(db: Session, skip: int = 0, limit: int = 100) -> list[models.Service]:
    return db.query(models.Service).offset(skip).limit(limit).all()

def get_service(db: Session, service_id: int) -> models.Service:
    return db.query(models.Service).filter(models.Service.id == service_id).first()

def create_service(db: Session, service: schemas.ServiceCreate) -> models.Service:
    db_service = models.Service(**service.model_dump())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)

    return db_service

def update_service(db: Session, service_id: int, service_update:schemas.ServiceUpdate) -> models.Service:
    db_service = get_service(db, service_id=service_id)
    if db_service is not None:
        db_service.name = service_update.name
        db_service.duration_in_slots = service_update.duration_in_slots
        db.commit()

    return db_service

def delete_service(db: Session, service_id: int) -> models.Service:
    db_service = get_service(db, service_id=service_id)
    if db_service is not None:
        db.delete(db_service)
        db.commit()

    return db_service


# Slot operations.
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
