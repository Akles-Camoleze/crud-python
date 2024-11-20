from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.db import Database


class Pessoa(Database.get_base()):
    __tablename__ = 'tb_pessoa'
    __table_args__ = {'schema': 'crud'}  # Define o schema

    id = Column(Integer, primary_key=True, nullable=False, name='pe_id')
    nome = Column(String(50), nullable=False, name='pe_nome')
    sobrenome = Column(String(255), nullable=False, name='pe_sobrenome')
    idade = Column(Integer, nullable=False, name='pe_idade')
    cpf = Column(String(11), unique=True, nullable=False, name='pe_cpf')

    disp_pessoas = relationship('DispositivoPessoa', back_populates="pessoa")