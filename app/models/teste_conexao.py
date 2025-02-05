from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Defina a URL de conexão com o banco de dados
database_url = "mysql+pymysql://root@localhost/test"  # Alterar se necessário
engine = create_engine(database_url, echo=True)

try:
    # Tentar conectar ao banco de dados
    with engine.connect() as connection:
        print("Conexão bem-sucedida ao banco de dados!")
except OperationalError as e:
    print(f"Erro na conexão: {e}")
