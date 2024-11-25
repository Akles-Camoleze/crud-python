from typing import TypeVar, Generic, List
from sqlalchemy.exc import SQLAlchemyError

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

    def delete_by_id(self, id: int) -> int:
        session = self._db.get_session()
        try:
            rows_deleted = session.query(self._entity).filter(self._entity.id == id).delete()
            session.commit()
            return rows_deleted
        except Exception as e:
            session.rollback()
            raise e

    def save(self, entity: T) -> T:
        session = self._db.get_session()
        try:
            if entity.id:
                session.merge(entity)
            else:
                session.add(entity)

            session.commit()
            return entity
        except SQLAlchemyError as e:
            session.rollback()
            raise e