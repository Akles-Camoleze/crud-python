from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Dispositivo(Base):
    __tablename__ = 'tb_dispositivo'
    __table_args__ = {'schema': 'crud'}  # Define o schema

    di_id = Column(Integer, primary_key=True, nullable=False)
    di_nome = Column(String(255), unique=True, nullable=False)