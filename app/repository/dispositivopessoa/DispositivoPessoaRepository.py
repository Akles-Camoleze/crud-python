from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.repository.BaseRepository import BaseRepository

class DispositivoPessoaRepository(BaseRepository[DispositivoPessoa]):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DispositivoPessoaRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__(DispositivoPessoa)
            self._initialized = True
