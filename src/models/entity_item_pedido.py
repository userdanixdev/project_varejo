# Entidade associativa (ItemPedido):

from sqlalchemy import Column, Integer, Float, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from src.database.base import Base

class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    id_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"),primary_key=True)
    id_produto = Column (Integer, ForeignKey("produtos.id_produto"), primary_key=True)
    quantidade = Column(Numeric(10,2), nullable=False)
    preco_unitario = Column(Numeric(10,2), nullable=False)

    # Relacionamentos:
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_pedido")
    
