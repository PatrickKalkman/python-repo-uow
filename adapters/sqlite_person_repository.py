from typing import Optional
import sqlite3

from adapters.base_repository import BaseRepository
from domain.person import Person


class SQLitePersonRepository(BaseRepository[Person]):
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection: sqlite3.Connection = connection
        self._create_table()

    def _create_table(self) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """
        )
        self.connection.commit()

    def add(self, item: Person) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO persons (name, age) VALUES (?, ?)",
            (item.name, item.age),
        )
        item.id = cursor.lastrowid

    def get_by_id(self, item_id: int) -> Optional[Person]:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, name, age FROM persons WHERE id=?", (item_id,)
        )
        row = cursor.fetchone()
        if row:
            return Person(row[1], row[2], row[0])
        return None

    def update(self, item: Person) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE persons SET name=?, age=? WHERE id=?",
            (item.name, item.age, item.id),
        )

    def delete(self, item_id: int) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute("DELETE FROM persons WHERE id=?", (item_id,))
