from datetime import date

from pydantic import BaseModel, EmailStr
from typing import Optional


# Auth classes.
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    hashed_password: str


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
