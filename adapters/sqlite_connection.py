import sqlite3
from adapters.base_connection import BaseConnection


class SQLiteConnection(BaseConnection):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection: sqlite3.Connection = connection

    def commit(self) -> None:
        self.connection.commit()

    def rollback(self) -> None:
        self.connection.rollback()
