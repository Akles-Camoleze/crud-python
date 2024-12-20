from typing import List

from app.entities.dispositivo.Dispositivo import Dispositivo
from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.entities.pessoa.Pessoa import Pessoa
from app.repository.BaseRepository import BaseRepository
from sqlalchemy.orm import joinedload

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

    def find_by_id_pessoa(self, pessoa_id) -> List[DispositivoPessoa]:
        session = self._db.get_session()
        return session.query(self._entity).join(Dispositivo).join(Pessoa) \
                .options(joinedload(DispositivoPessoa.dispositivo)) \
                .filter(Pessoa.id == pessoa_id).all()
