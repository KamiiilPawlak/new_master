from typing import Generic, TypeVar
from random import randint

Number = TypeVar("Number", int, float)
T = Generic[TypeVar("T")]

def add(a: Number, b: Number) -> Number:
    return a + b 

print(add(randint(0, 10), randint(10, 100)))

print(type(Number))