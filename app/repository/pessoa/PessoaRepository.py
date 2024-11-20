from app.entities.pessoa.Pessoa import Pessoa
from app.repository.BaseRepository import BaseRepository

class PessoaRepository(BaseRepository[Pessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PessoaRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(Pessoa)
            self._initialized = True
