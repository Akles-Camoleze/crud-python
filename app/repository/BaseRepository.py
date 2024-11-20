from typing import TypeVar, Generic, List

from app.db.db import Database

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, entity: T):
        self._entity = entity
        self._db = Database()

    def find_all(self) -> List[T]:
        session = self._db.get_session()
        return session.query(self._entity).all()

    def find_by_id(self, id) -> T:
        session = self._db.get_session()
        return session.query(self._entity).filter(self._entity.id == id).first()
