import string

from adapters.base_repository import BaseRepository
from domain.person import Person


class SQLitePersonRepository(BaseRepository[Person]):
    def __init__(self, connection):
        self.connection = connection
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                person_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                FOREIGN KEY (person_id) REFERENCES persons (id)
            )
        ''')
        self.connection.commit()

    def add(self, person: Person):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO persons (id, name, age) VALUES (?, ?, ?)",
            (person.id, person.name, person.age)
        )
        person.id = cursor.lastrowid

    def get_by_id(self, person_id: string) -> Person:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, age FROM persons WHERE id=?",
                       (person_id))
        row = cursor.fetchone()
        if row:
            return Person(row[1], row[2], row[0])

    def update(self, person: Person):
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE persons SET name=?, age=? WHERE id=?",
            (person.name, person.age, person.id)
        )

    def delete(self, person_id: string):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM persons WHERE id=?", (person_id))
