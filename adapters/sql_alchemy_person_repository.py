from typing import Optional
from sqlalchemy.orm import Session

from adapters.base_repository import BaseRepository
from domain.person import Person


class SQLAlchemyPersonRepository(BaseRepository[Person]):
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def add(self, item: Person) -> None:
        self.session.add(item)
        # flush() is needed to get the id of the person
        self.session.flush()

    def update(self, item: Person) -> None:
        self.session.merge(item)

    def delete(self, item_id: int) -> None:
        person: Person | None = self.session.get(Person, item_id)
        if person:
            self.session.delete(person)

    def get_by_id(self, item_id: int) -> Optional[Person]:
        return self.session.get(Person, item_id)
