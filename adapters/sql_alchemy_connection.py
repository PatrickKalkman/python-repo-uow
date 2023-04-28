from sqlalchemy.orm import Session
from adapters.base_connection import BaseConnection


class SQLAlchemyConnection(BaseConnection):
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
