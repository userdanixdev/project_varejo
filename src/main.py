# Executável para gerar as tabelas do banco de dados:

from src.database.connection import engine
from src.database.base import Base

from src.models.entity_fornecedor import Fornecedor
from src.models.entity_cliente import Cliente
from src.models.entity_produto import Produto
from src.models.entity_pedido import Pedido
from src.models.entity_item_pedido import ItemPedido

def criar_tabelas():
    Base.metadata.create_all(engine)

if __name__== "__main__":
    criar_tabelas()
