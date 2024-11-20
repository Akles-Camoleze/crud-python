from app.entities.Pessoa import Pessoa
from app.repository.BaseRepository import BaseRepository

class PessoaRepository(BaseRepository[Pessoa]):
    def __init__(self):
        super().__init__(Pessoa)