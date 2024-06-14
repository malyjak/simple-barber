from datetime import date

from pydantic import BaseModel, EmailStr
from typing import Optional


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
