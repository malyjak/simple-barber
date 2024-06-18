from datetime import date

from pydantic import BaseModel, EmailStr
from typing import Optional


# Service classes.
class ServiceBase(BaseModel):
    name: str
    duration_in_slots: int

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(ServiceBase):
    pass

class Service(ServiceBase):
    id: int


# Slot classes.
class SlotBase(BaseModel):
    date: date
    occupied: Optional[bool] = False

class SlotCreate(SlotBase):
    pass

class SlotUpdate(SlotBase):
    pass

class Slot(SlotBase):
    id: int


class ReservationBase(BaseModel):
    slot_id: int
    full_name: str
    phone_number: str
    email: EmailStr
    note: Optional[str] = None
