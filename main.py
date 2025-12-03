from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Any, Generic, TypeVar
from random import randint
import re

# more 

class Event(BaseModel):
    name: str
    place: str
    how_much_ticket: int
    data_start: datetime


    @field_validator("name")
    def validate_name(cls, v: str) -> str:
        if not re.fullmatch(r"[A-Za-z1-9]{2,50}", v):
            raise ValueError(
                "Name must be 2-30 characters long and contain only A-Z, a-z, 1-9"
            )
        return v


    @field_validator('place')
    def validate_place(cls, v: str) -> str:
        if not re.fullmatch(r"[A-Za-z]{2,15}", v):
            raise ValueError(
                "Name place must be 2-15 characters long and contain only A-Z, a-z"
            )
        
        return v
    

    @field_validator("how_much_ticket")
    def validator_how_much(cls, v) -> int:
        if v == 0:
            raise ValueError("Empty :(")
        elif v < 0:
            raise ValueError("Nie moze byc mniejsza od 0")
        elif v > 0 and v < 5:
            raise ValueError("Max mozesz wziac 5 biletow jednoczesnie")
        
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


krawczyk = Event(name = "Krzysztof", 
                 place= 'KRK', 
                 how_much_ticket=4,  
                 data_start = datetime(2025, 12, 20))

print(krawczyk.model_dump_json())
print(krawczyk.model_json_schema())