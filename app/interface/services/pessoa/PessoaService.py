from app.controller.pessoa.PessoaController import PessoaController
from app.entities.pessoa.Pessoa import Pessoa
from app.interface.services.BaseService import BaseService


class PessoaService(BaseService[Pessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PessoaService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(PessoaController())
            self._initialized = True