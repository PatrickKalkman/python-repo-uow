from abc import ABC, abstractmethod


class BaseConnection(ABC):
    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError()
