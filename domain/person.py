from dataclasses import dataclass
from typing import Optional


@dataclass
class Person:
    id: Optional[int]
    name: str
    age: int
