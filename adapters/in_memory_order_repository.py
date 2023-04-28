from typing import Optional
from adapters.base_repository import BaseRepository
from domain.order import Order


class InMemoryOrderRepository(BaseRepository[Order]):
    def __init__(self) -> None:
        self.orders: dict[int, Order] = {}

    def add(self, item: Order) -> None:
        id: int = item.id if item.id is not None else 0
        self.orders[id] = item

    def get_by_id(self, item_id: int) -> Optional[Order]:
        return self.orders.get(item_id)

    def update(self, item: Order) -> None:
        id: int = item.id if item.id is not None else 0
        self.orders[id] = item

    def delete(self, item_id: int) -> None:
        self.orders.pop(item_id, None)
