from typing import List

from app.controller.dispositivopessoa.DispositivoPessoaController import DispositivoPessoaController
from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.interface.services.BaseService import BaseService


class DispositivoPessoaService(BaseService[DispositivoPessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoPessoaService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._controller = DispositivoPessoaController()
            super().__init__(self._controller)
            self._initialized = True

    def find_by_id_pessoa(self, pessoa_id) -> List[DispositivoPessoa]:
        return self._controller.find_by_id_pessoa(pessoa_id)