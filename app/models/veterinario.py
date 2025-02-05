from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir a URL de conexão com o banco de dados
database_url = "mysql+pymysql://root@localhost/test"
engine = create_engine(database_url, echo=True)

# Definir a base para as classes de banco de dados
Base = declarative_base()

class Veterinario(Base):
    __tablename__ = "veterinario"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_completo = Column("nome_completo", String(200), nullable=False)
    data_nascimento = Column("data_nascimento", Date, nullable=False)
    genero = Column("genero", String(20), nullable=False)
    email = Column("email", String(100), unique=True, nullable=False)
    telefone = Column("telefone", String(15), nullable=False)
    formacao_academica = Column("formacao_academica", Text)
    especializacao = Column("especializacao", Text)
    senha = Column("senha", String(15), nullable=False)
    endereco = Column("endereco", Text)
    observacoes = Column("observacoes", Text)

    def __init__(self, nome_completo, data_nascimento, genero, email, telefone, formacao_academica, especializacao, senha, endereco, observacoes):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.genero = genero
        self.email = email
        self.telefone = telefone
        self.formacao_academica = formacao_academica
        self.especializacao = especializacao
        self.senha = senha
        self.endereco = endereco
        self.observacoes = observacoes

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
