from app.controller.BaseController import BaseController
from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.repository.DispositivoPessoaRepository import DispositivoPessoaRepository


class DispositivoPessoaController(BaseController[DispositivoPessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoPessoaController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(DispositivoPessoaRepository())
            self._initialized = True
