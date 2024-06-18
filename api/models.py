from sqlalchemy import Column, Integer, Date, Boolean, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    duration_in_slots = Column(Integer, nullable=True)

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=True)
    occupied = Column(Boolean, nullable=True)

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    slot_id = Column(Integer, nullable=True)
    full_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    note = Column(String, nullable=True)
