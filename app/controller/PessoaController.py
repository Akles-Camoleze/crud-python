from app.controller.BaseController import BaseController
from app.entities.pessoa.Pessoa import Pessoa
from app.repository.PessoaRepository import PessoaRepository

class PessoaController(BaseController[Pessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PessoaController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(PessoaRepository())
            self._initialized = True
