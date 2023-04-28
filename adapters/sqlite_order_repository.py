from typing import Optional
import sqlite3
from domain.order import Order
from adapters.base_repository import BaseRepository


class SQLiteOrderRepository(BaseRepository[Order]):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection: sqlite3.Connection = connection
        self._create_table()

    def _create_table(self):
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                FOREIGN KEY (person_id) REFERENCES persons (id)
            )
        """
        )
        self.connection.commit()

    def add(self, item: Order) -> None:
        query = """
        INSERT INTO orders (person_id, order_date, total_amount)
        VALUES (?, ?, ?)
        """
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(
            query, (item.person_id, item.order_date, item.total_amount)
        )
        item.id = cursor.lastrowid

    def update(self, item: Order) -> None:
        query = """
        UPDATE orders
        SET person_id = ?, order_date = ?, total_amount = ?
        WHERE id = ?
        """
        self.connection.execute(
            query,
            (item.person_id, item.order_date, item.total_amount, item.id),
        )

    def delete(self, item_id: int) -> None:
        query = "DELETE FROM orders WHERE id = ?"
        self.connection.execute(query, (item_id,))

    def get_by_id(self, item_id: int) -> Optional[Order]:
        query = """
        SELECT id, person_id, order_date, total_amount
        FROM orders WHERE id = ?
        """
        cursor: sqlite3.Cursor = self.connection.execute(query, (item_id,))
        row = cursor.fetchone()
        if row:
            return Order(
                id=row[0],
                person_id=row[1],
                order_date=row[2],
                total_amount=row[3],
            )
        return None
