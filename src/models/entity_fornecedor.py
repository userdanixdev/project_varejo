# Formatação das tabelas do banco de dados:

from sqlalchemy import Column, Integer, String
from src.database.base import Base
from sqlalchemy.orm import relationship

class Fornecedor(Base):
    __tablename__='fornecedores'
    id_fornecedor = Column(Integer, primary_key=True)
    nome_fantasia = Column(String(100), nullable=False)
    cnpj = Column(String(18),unique=True,nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))     

    produtos = relationship ("Produto",back_populates="fornecedor")   
