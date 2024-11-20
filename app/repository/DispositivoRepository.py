from app.entities.Dispositivo import Dispositivo
from app.repository.BaseRepository import BaseRepository

class DispositivoRepository(BaseRepository[Dispositivo]):
    def __init__(self):
        super().__init__(Dispositivo)