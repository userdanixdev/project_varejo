# Entidade associativa (ItemPedido):

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.database.base import Base

class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    id_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"),primary_key=True)
    id_produto = Column (Integer, ForeignKey("produtos.id_produto"), primary_key=True)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)

    # Relacionamentos:
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_pedido")
    
