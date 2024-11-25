from typing import List

from app.controller.BaseController import BaseController
from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.repository.dispositivopessoa.DispositivoPessoaRepository import DispositivoPessoaRepository


class DispositivoPessoaController(BaseController[DispositivoPessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoPessoaController, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._repository = DispositivoPessoaRepository()
            super().__init__(self._repository)
            self._initialized = True

    def find_by_id_pessoa(self, pessoa_id) -> List[DispositivoPessoa]:
        return self._repository.find_by_id_pessoa(pessoa_id)
