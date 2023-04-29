import sqlite3
from domain.person import Person
from adapters.sqlite_person_repository import SQLitePersonRepository
import pytest


@pytest.fixture
def connection():
    conn: sqlite3.Connection = sqlite3.connect(":memory:")
    yield conn
    conn.close()


@pytest.fixture
def repository(connection: sqlite3.Connection) -> SQLitePersonRepository:
    return SQLitePersonRepository(connection)


def test_add_person(repository: SQLitePersonRepository) -> None:
    person = Person(name="John Doe", age=30)
    repository.add(person)

    assert person.id is not None
    retrieved_person: Person | None = repository.get_by_id(person.id)
    assert retrieved_person is not None
    assert retrieved_person.name == person.name
    assert retrieved_person.age == person.age


def test_update_person(repository: SQLitePersonRepository) -> None:
    person = Person(name="John Doe", age=30)
    repository.add(person)

    person.name = "Jane Doe"
    person.age = 28
    repository.update(person)

    assert person.id is not None
    updated_person: Person | None = repository.get_by_id(person.id)
    assert updated_person is not None
    assert updated_person.name == "Jane Doe"
    assert updated_person.age == 28


def test_delete_person(repository: SQLitePersonRepository) -> None:
    person = Person(name="John Doe", age=30)
    repository.add(person)
    assert person.id is not None
    repository.delete(person.id)

    deleted_person: Person | None = repository.get_by_id(person.id)
    assert deleted_person is None


def test_get_by_id_person_not_found(
    repository: SQLitePersonRepository,
) -> None:
    non_existent_person: Person | None = repository.get_by_id(999)
    assert non_existent_person is None
