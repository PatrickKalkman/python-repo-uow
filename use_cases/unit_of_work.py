from types import TracebackType
from adapters.base_connection import BaseConnection
from adapters.base_repository import BaseRepository
from domain.order import Order
from domain.person import Person


class UnitOfWork:
    def __init__(
        self,
        connection: BaseConnection,
        person_repository: BaseRepository[Person],
        order_repository: BaseRepository[Order],
    ) -> None:
        self.persons: BaseRepository[Person] = person_repository
        self.orders: BaseRepository[Order] = order_repository
        self.connection: BaseConnection = connection

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()

    def commit(self) -> None:
        self.connection.commit()

    def rollback(self) -> None:
        self.connection.rollback()
