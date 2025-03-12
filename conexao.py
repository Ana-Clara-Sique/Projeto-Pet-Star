from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt #importa o bcrypt para verifiar a senha

# URL de Conexão com o banco de dados MySQL no XAMPP
DATABASE_URL = "mysql+pymysql://root:@localhost/petstar"  

# Criar a base para os modelos
Base = declarative_base()

# Definir a classe de modelo para a tabela 'usuarios'
class Usuario(Base):
    __tablename__ = 'usuarios-veterinarios1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(150), nullable=False)  # Nome completo
    email = Column(String(100), nullable=False)
    login = Column(String(50), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)  # Data de nascimento
    genero = Column(String(20), nullable=True)  # Gênero
    telefone = Column(String(20), nullable=True)  # Telefone
    formacao_academica = Column(String(100), nullable=True)  # Formação acadêmica
    especializacao = Column(String(100), nullable=True)  # Especialização
    observacoes = Column(Text, nullable=True)  # Observações

# Criar a conexão com o banco de dados MySQL
engine = create_engine(DATABASE_URL)

# Criar todas as tabelas no banco de dados (se não existirem)
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)

# Função para cadastrar um usuário
def cadastrar_veterinario(nome_completo, email, login, senha, data_nascimento, genero, telefone, formacao_academica, especializacao, observacoes):
    session = Session()  # Criando uma nova sessão

 # Verificar se o login já existe
    usuario_existente = session.query(Usuario).filter_by(login=login).first()
    if usuario_existente:
        session.close()
        raise ValueError("O login já está em uso. Escolha outro.")

# Criptografar a senha antes de salvar
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    #Cria um novo usuario 
    novo_usuario = Usuario(
        nome_completo=nome_completo, email=email, login=login, senha=senha_hash,
        data_nascimento=data_nascimento, genero=genero, telefone=telefone,
        formacao_academica=formacao_academica, especializacao=especializacao,
        observacoes=observacoes
    )
    session.add(novo_usuario)
    session.commit()  # Comita as mudanças no banco
    session.close()  # Fecha a sessão após o commit
    print("Usuário cadastrado com sucesso!")

# Função para verificar login e senha
def verificar_login(login, senha=None):
    session = Session()  # Criando uma nova sessão
    usuario = session.query(Usuario).filter_by(login=login).first()
    session.close()  # Fecha a sessão após a consulta
    
    if usuario:
        # Verifica se a senha fornecida corresponde à senha armazenada (hash)
        if senha and bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
            return True
    
    return False
