from flask import Flask, render_template, request, redirect, url_for
from conexao import cadastrar_veterinario, verificar_login # Importando as funções do banco de dados

app = Flask(__name__,
             template_folder='app/templates', 
             static_folder='app/static')

# Rota para a página inicial (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de cadastro (cadastro.html)
@app.route('/cadastrar_veterinario', methods=['GET', 'POST'])
def cadastrar_veterinario_form():
    if request.method == 'POST':
        print("Formulário enviado com método POST")
        nome_completo = request.form['nome_completo']
        email = request.form['email']
        login = request.form['login']
        senha = request.form['senha']
        data_nascimento = request.form['data_nascimento']
        genero = request.form['genero']
        telefone = request.form['telefone']
        formacao_academica = request.form['formacao_academica']
        especializacao = request.form['especializacao']
        observacoes = request.form['observacoes']
        
        if verificar_login(login, senha):  # Verifica se o login já existe
            return "Usuário já cadastrado!"
        
        cadastrar_veterinario (nome_completo, email, login, senha, data_nascimento, genero, telefone, formacao_academica, especializacao, observacoes)  # Cadastra o novo usuário no banco
        return redirect(url_for('entrar'))

    
    return render_template('cadastrar_veterinario.html')

# Rota para a página de login (entrar.html)
@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        
        if verificar_login(login, senha):  # Verifica se o login e senha estão corretos
            return redirect(url_for('pagina_principal_vet'))  # Redireciona para a página inicial do usuário
        else:
            return "Usuário ou senha inválidos!"
    
    return render_template('entrar.html')



# Rota para a página principal do veterinário (pagina-principal-vet.html)
@app.route('/pagina-principal-vet/<nome>')  # Alteração aqui
def pagina_principal_vet(nome):
    return render_template('pagina-principal-vet.html', nome=nome)


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
@app.route('/cadastrar-veterinario')
def cadastrar_veterinario():
   return render_template('cadastrar-veterinario.html')

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
    return render_template('cadastro-servicos.html')

# Rota para a página de histórico de serviços (historico-de-servicos.html)
@app.route('/historico-de-servicos')
def historico_de_servicos():
    return render_template('historico-de-servicos.html')

# Rota para a página de perfil do veterinário (perfil-veterinario.html)
@app.route('/perfil-veterinario')
def perfil_veterinario():
    return render_template('perfil-veterinario.html')

if __name__ == '__main__':
    app.run(debug=True)
