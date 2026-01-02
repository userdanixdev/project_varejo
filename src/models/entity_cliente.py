# Formatação das tabelas do banco de dados:

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.database.base import Base
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__= 'clientes'
    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14),unique=True, nullable=False)
    telefone = Column(String(14),unique=True,nullable=False)
    email = Column(Integer, nullable = False)
    
    # Relacionamentos: A entidade Cliente precisa se relacionar com a entidade Pedidos
    pedidos = relationship("Pedido", back_populates="cliente")
    