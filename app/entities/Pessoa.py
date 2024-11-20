from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'tb_pessoa'
    __table_args__ = {'schema': 'crud'}  # Define o schema

    pe_id = Column(Integer, primary_key=True, nullable=False)
    pe_nome = Column(String(50), nullable=False)
    pe_sobrenome = Column(String(255), nullable=False)
    pe_idade = Column(Integer, nullable=False)
    pe_cpf = Column(String(11), unique=True, nullable=False)