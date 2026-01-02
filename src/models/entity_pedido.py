# Tabela Pedido:

from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.database.base import Base

class Pedido(Base):
    __tablename__ = 'pedidos'
    id_pedido = Column(Integer, primary_key=True)
    data_pedido = Column(DateTime, default=datetime.utcnow)
    valor_total = Column(Float, nullable=False)
    # Chave estrangeira da entidade Cliente por ter relação direta:
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"),nullable=False)
    # Relacionamentos:
    cliente = relationship("Cliente", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido")
    