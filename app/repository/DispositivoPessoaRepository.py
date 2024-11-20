from app.entities.DispositivoPessoa import DispositivoPessoa
from app.repository.BaseRepository import BaseRepository

class DispositivoPessoaRepository(BaseRepository[DispositivoPessoa]):
    def __init__(self):
        super().__init__(DispositivoPessoa)