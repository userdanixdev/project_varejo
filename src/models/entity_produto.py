# Formatação das tabelas do banco de dados:

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Numeric, VARCHAR, CHAR
from src.database.base import Base
from sqlalchemy.orm import relationship

class Produto(Base):
    __tablename__= 'produtos'
    id_produto = Column(Integer, primary_key=True)
    nome = Column(CHAR(100), nullable=False)
    categoria = Column(CHAR(18))
    preco = Column(Numeric(10,2),nullable = False)
    quantidade_estoque = Column(Integer, nullable = False)
    # Coluna de chave estrangeira da entidade Fornecedor de relação direta:
    id_fornecedor = Column(Integer, ForeignKey("fornecedores.id_fornecedor"), nullable=False)
    # Relacionamentos:
    fornecedor = relationship("Fornecedor", back_populates="produtos")
    itens_pedido = relationship("ItemPedido", back_populates="produto")