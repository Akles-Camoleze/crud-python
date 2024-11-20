from app.controller.BaseController import BaseController
from app.entities.dispositivo.Dispositivo import Dispositivo
from app.repository.dispositivo.DispositivoRepository import DispositivoRepository


class DispositivoController(BaseController[Dispositivo]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(DispositivoRepository())
            self._initialized = True