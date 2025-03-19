from flask import Flask, jsonify, render_template, request, redirect, session, url_for
import bcrypt # pra importar o bcrypt para as senhas
from conexao import Session, Usuario, cadastrar_veterinario, verificar_login # Importando as funções do banco de dados

app = Flask(__name__,
             template_folder='app/templates', 
             static_folder='app/static')

app.secret_key = 'sua_chave_secreta_aqui'  # Adicione uma chave secreta para as sessões

import os
print(os.path.join(os.getcwd(), 'app', 'templates'))



# Rota para a página inicial (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de cadastro (cadastro.html)
# Rota para a página de cadastro (cadastro.html)
@app.route('/cadastrar-veterinario', methods=['GET', 'POST'])
def cadastrar_veterinario_view():
    if request.method == 'POST':
        print("Formulário enviado com método POST")
        nome_completo = request.form['nome_completo']
        email = request.form['email']
        login = request.form['login']
        senha = request.form['senha']  # Apenas recebe a senha simples
        data_nascimento = request.form['data_nascimento']
        genero = request.form['genero']
        telefone = request.form['telefone']
        formacao_academica = request.form['formacao_academica']
        especializacao = request.form['especializacao']
        observacoes = request.form['observacoes']

        # Verifica se o login já existe
        if verificar_login(login, senha):
            return "Usuário já cadastrado!"

        # Remova o hashing da senha aqui, a função cadastrar_veterinario fará isso
        try:
            # Agora passa a senha simples para a função cadastrar_veterinario
            cadastrar_veterinario(nome_completo, email, login, senha, data_nascimento, genero, telefone, formacao_academica, especializacao, observacoes)
            return redirect(url_for('entrar'))  # Redireciona para a página de login após o cadastro
        except Exception as e:
            # Caso haja erro ao cadastrar, exibe uma mensagem
            return f"Erro ao cadastrar veterinário: {str(e)}"

    else:
        # Caso o método seja GET, apenas renderiza a página de cadastro
        return render_template('cadastrar-veterinario.html')

# Rota para a página de login (entrar.html)
@app.route('/Entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        
        if verificar_login(login, senha):  # Verifica se o login e senha estão corretos
            #Armazenando o login na sessao
            session['login'] = login  # Aqui, armazena o login ou outro dado que ajude a identificar o usuário
            return redirect(url_for('pagina_principal_vet'))  # Redireciona para a página inicial do usuário
        else:
            return "Usuário ou senha inválidos!"
    
    return render_template('Entrar.html')



# Endpoint para listar todos os veterinários
@app.route('/api/veterinarios', methods=['GET'])
def listar_veterinarios():
    session = Session()
    veterinarios = session.query(Usuario).all()  # Assume-se que a classe Usuario seja o modelo de Veterinário
    session.close()
    return jsonify([veterinario.as_dict() for veterinario in veterinarios])

# Endpoint para obter detalhes de um veterinário pelo ID
@app.route('/api/veterinarios/<int:id>', methods=['GET'])
def obter_veterinario(id):
    session = Session()
    veterinario = session.query(Usuario).filter_by(id=id).first()  # Recupera pelo ID
    session.close()
    if veterinario:
        return jsonify(veterinario.as_dict())
    return jsonify({'error': 'Veterinário não encontrado'}), 404

# Rota para a página principal do veterinário (pagina-principal-vet.html)
@app.route('/pagina-principal-vet')  # Alteração aqui
def pagina_principal_vet():
     if 'login' not in session:  # Verifica se o login está armazenado na sessão
        return redirect(url_for('entrar'))  # Se não estiver logado, redireciona para a página de login
 # Caso o usuário esteja logado, renderiza a página principal.
     return render_template('pagina-principal-vet.html')
   


#@app.route('/pagina-principal-vet')
#def pagina_principal_vet(nome):
# #return render_template('pagina-principal-vet.html', nome=nome)

# Rota para a página principal após login (home.html)
#@app.route('/home/<nome>')
#def home(nome):
    #return render_template('home.html', nome=nome)

# Rota para a página de contato (contato.html)
@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota para a página de serviços (servicos.html)
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

# Rota para a página de login (entrar.html)
#@app.route('/entrar')
#def entrar():
#return render_template('entrar.html')

# Rota para cadastro de veterinário (cadastrar-veterinario.html)
#@app.route('/cadastrar-veterinario')
#def cadastrar_veterinario():
#return render_template('cadastrar-veterinario.html')

# Rota para a página de clientes (clientes.html)
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

# Rota para a página de pets (pets.html)
@app.route('/pets')
def pets():
    return render_template('pets.html')

# Rota para a página de agendamentos (agendamentos.html)
@app.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html')

# Rota para a página de prontuários (prontuarios.html)
@app.route('/prontuarios')
def prontuarios():
    return render_template('prontuarios.html')

# Rota para a página de cadastro de serviços (cadastro-servicos.html)
@app.route('/cadastro-servicos')
def cadastro_servicos():
    return render_template('cadastro-serviços.html')

# Rota para a página de histórico de serviços (historico-de-servicos.html)
@app.route('/historico-de-servicos')
def historico_de_servicos():
    return render_template('historico-de-serviços.html')

# Rota para a página de perfil do veterinário (perfil-veterinario.html)
@app.route('/perfil-veterinario')
def perfil_veterinario():
     if 'login' not in session:  # Verifica se o usuário não está logado
        return redirect(url_for('entrar'))  # Redireciona para a página de login
     return render_template('perfil-veterinario.html') #caso o usuario esteja logado,exibe o perfil

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('login', None)  # Remove o login da sessão
    return redirect(url_for('index'))  # Redireciona para a página inicial

@app.route('/autor')
def autor():
    return jsonify({
        'nome': 'Ana Clara',
        'email': 'ana.siqueira62@aluno.ifce.edu.br',
        'descricao': 'Projeto Pet Star - Responsavel pela entidade veterinario'
    })


if __name__ == '__main__':
    app.run(debug=True)
