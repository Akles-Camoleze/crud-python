from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.db import Database


class DispositivoPessoa(Database.get_base()):
    __tablename__ = 'tb_disp_pessoa'
    __table_args__ = {'schema': 'crud'}

    id = Column(Integer, primary_key=True, nullable=False, name='dpe_id')
    di_id = Column(Integer, ForeignKey('crud.tb_dispositivo.di_id', ondelete="CASCADE"), nullable=False, name='di_id')
    pe_id = Column(Integer, ForeignKey('crud.tb_pessoa.pe_id', ondelete="CASCADE"), nullable=False, name='pe_id')

    dispositivo = relationship('Dispositivo', back_populates="disp_pessoas")
    pessoa = relationship('Pessoa', back_populates="disp_pessoas")