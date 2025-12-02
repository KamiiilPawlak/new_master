from pydantic import BaseModel, field_validator, Field
from datetime import datetime
from typing import Generic, TypeVar
from random import randint
import re


class Event(BaseModel):
    name: str
    data_start: datetime

    @field_validator("name")
    def validate_name(cls, v: str) -> str:
        if not re.fullmatch(r"[A-Za-z1-9]{2,30}", v):
            raise ValueError(
                "Name must be 2-30 characters long and contain only A-Z, a-z, 1-9"
            )
        return v

    @field_validator('data_start')
    def event_must_later_than_today(cls, value):
        if value < datetime.today():
            raise ValueError("Date must be later than today")
        
        return value

Number = TypeVar("Number", int, float)
T = Generic[TypeVar("T")]

def add(a: Number, b: Number) -> Number:
    return a + b 

print(add(randint(0, 10), randint(10, 100)))

print(type(Number))
print(datetime.today())