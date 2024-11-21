from typing import TypeVar, Generic, List

from app.controller.BaseController import BaseController

T = TypeVar('T')

class BaseService(Generic[T]):
    def __init__(self, repository: BaseController[T]):
        self._controller = repository

    def find_all(self) -> List[T]:
        return self._controller.find_all()

    def find_by_id(self, id) -> T:
        return self._controller.find_by_id(id)

    def delete_by_id(self, id) -> int:
        return self._controller.delete_by_id(id)