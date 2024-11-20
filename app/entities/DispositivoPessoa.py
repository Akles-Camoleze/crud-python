from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class DispositivoPessoa(Base):
    __tablename__ = 'tb_disp_pessoa'
    __table_args__ = {'schema': 'crud'}  # Define o schema

    dpe_id = Column(Integer, primary_key=True, nullable=False)
    di_id = Column(Integer, ForeignKey('crud.tb_dispositivo.di_id', ondelete="CASCADE"), nullable=False)
    pe_id = Column(Integer, ForeignKey('crud.tb_pessoa.pe_id', ondelete="CASCADE"), nullable=False)