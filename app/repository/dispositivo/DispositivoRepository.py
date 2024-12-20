from typing import List

from app.entities.dispositivo.Dispositivo import Dispositivo
from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.entities.pessoa.Pessoa import Pessoa
from app.repository.BaseRepository import BaseRepository, T


class DispositivoRepository(BaseRepository[Dispositivo]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(Dispositivo)
            self._initialized = True
