# Formatação das tabelas do banco de dados:

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.database.base import Base
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__= 'produtos'
    id_produto = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(18))
    preco = Column(Float,nullable = False)
    quantidade_estoque = Column(Integer, nullable = False)
    # Coluna de chave estrangeira da entidade Fornecedor de relação direta:
    id_fornecedor = Column(Integer, ForeignKey("fornecedores.id_fornecedor"), nullable=False)
    # Relacionamentos:
    fornecedor = relationship("Fornecedor", back_populates="produtos")
    itens_pedido = relationship("ItemPedido", back_populates="produto")