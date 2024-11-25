from app.repository.BaseRepository import BaseRepository

from typing import TypeVar, Generic, List

T = TypeVar('T')

class BaseController(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self._repository: BaseRepository[T] = repository

    def find_all(self) -> List[T]:
        return self._repository.find_all()

    def find_by_id(self, id) -> T:
        return self._repository.find_by_id(id)

    def delete_by_id(self, id) -> int:
        return self._repository.delete_by_id(id)

    def save(self, entity: T) -> T:
        return self._repository.save(entity)