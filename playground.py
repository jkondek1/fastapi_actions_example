from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person(name="John", age="25")
print(person)

from pydantic import BaseModel, Field


class PersonP(BaseModel):
    name: str
    age: int = Field(strict=True)


person = PersonP(name="John", age="25")
print(person)
