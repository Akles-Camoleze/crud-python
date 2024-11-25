from typing import List

from app.controller.dispositivo.DispositivoController import DispositivoController
from app.entities.dispositivo.Dispositivo import Dispositivo
from app.interface.services.BaseService import BaseService


class DispositivoService(BaseService[Dispositivo]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._controller = DispositivoController()
            super().__init__(self._controller)
            self._initialized = True
