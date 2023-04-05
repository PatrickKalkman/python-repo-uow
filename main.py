from contextlib import contextmanager
import sqlite3

from sqlite_person_repository import SQLitePersonRepository
from sqlite_order_repository import SQLiteOrderRepository
from sqlite_connection import SQLiteConnection
from unit_of_work import UnitOfWork
from models.person import Person
from models.order import Order
from use_cases.create_person_and_order_use_case import CreatePersonAndOrderUseCase


@contextmanager
def create_database_connection():
    conn = sqlite3.connect("./db/data.db")
    try:
        yield conn
    finally:
        conn.close()


if __name__ == "__main__":
    with create_database_connection() as conn:
        connection = SQLiteConnection(conn)
        person_repository = SQLitePersonRepository(conn)
        order_repository = SQLiteOrderRepository(conn)

        unit_of_work = UnitOfWork(connection, person_repository, order_repository)
        create_person_and_order_use_case = CreatePersonAndOrderUseCase(unit_of_work)

        new_person = Person(name="John Doe", age=30)
        new_order = Order(person_id=None, order_date="2023-04-03", total_amount=100.0)

        created_person, created_order = create_person_and_order_use_case.execute(new_person, new_order)
