from dataclasses import dataclass
from typing import Optional


@dataclass
class Order:
    person_id: int
    order_date: str
    total_amount: float
    id: Optional[int] = None
