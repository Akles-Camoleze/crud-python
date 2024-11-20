from app.repository.BaseRepository import BaseRepository

class BaseController:
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def find_all(self):
        return self._repository.find_all()

    def find_by_id(self, id):
        return self._repository.find_by_id(id)
