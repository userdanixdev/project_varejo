# 1° = Criar a conexão DuckDB + SQLAlchemy:

from sqlalchemy import create_engine

DATABASE_URL = "duckdb:///smart_retail.duckdb"

engine = create_engine(DATABASE_URL, echo=True)

# Nota: O arquivo smart_retail.duckdb será criado automaticamente.