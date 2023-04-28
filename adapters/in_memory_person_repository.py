from typing import Optional
from adapters.base_repository import BaseRepository
from domain.person import Person


class InMemoryPersonRepository(BaseRepository[Person]):
    def __init__(self) -> None:
        self.persons: dict[int, Person] = {}

    def add(self, item: Person) -> None:
        id: int = item.id if item.id is not None else 0
        self.persons[id] = item

    def get_by_id(self, item_id: int) -> Optional[Person]:
        return self.persons.get(item_id)

    def update(self, item: Person) -> None:
        id: int = item.id if item.id is not None else 0
        self.persons[id] = item

    def delete(self, item_id: int) -> None:
        self.persons.pop(item_id, None)
