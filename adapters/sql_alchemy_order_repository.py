from typing import Optional
from sqlalchemy.orm import Session

from adapters.base_repository import BaseRepository
from domain.order import Order


class SQLAlchemyOrderRepository(BaseRepository[Order]):
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def add(self, item: Order) -> None:
        self.session.add(item)

    def update(self, item: Order) -> None:
        self.session.merge(item)

    def delete(self, item_id: int) -> None:
        order: Order | None = self.session.get(Order, item_id)
        if order:
            self.session.delete(order)

    def get_by_id(self, item_id: int) -> Optional[Order]:
        return self.session.get(Order, item_id)
