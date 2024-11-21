from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

from app.db.db import Database


class Dispositivo(Database.get_base()):
    __tablename__ = 'tb_dispositivo'
    __table_args__ = {'schema': 'crud'}

    id = Column(Integer, Sequence('seq_dispositivo', schema='crud'), primary_key=True, nullable=False, name='di_id')
    nome = Column(String(255), unique=True, nullable=False, name='di_nome')

    disp_pessoas = relationship('DispositivoPessoa', back_populates="dispositivo")