from dataclasses import dataclass


@dataclass
class Order:
    order_date: str
    total_amount: float
    person_id: int | None = None
    id: int | None = None
