from flask import Flask, render_template

app = Flask(__name__,
             template_folder='app/templates', 
             static_folder='app/static')

# Rota para pagina inicial(index.html)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para a pagina de contato(contato.html)

@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota para pagina de serviços(servicos.html)

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

# Rota para pagina de login(entrar.html)

@app.route('/entrar')
def entrar():
    return render_template('entrar.html')

# Rota para cadastro de veterinario


@app.route('/cadastrar-veterinario')
def cadastrar_veterinario():
    return render_template('cadastrar-veterinario.html')


# rota para agina principal

@app.route('/pagina-principal-vet')
def pagina_principal_vet():
    return render_template('pagina-principal-vet.html')


@app.route('/clientes')
def clientes():
    return render_template('clientes.html')



@app.route('/pets')
def pets():
    return render_template('pets.html')



@app.route('/agendamentos')
def agendamentos():
    return render_template('agendamentos.html')

@app.route('/prontuarios')
def prontuarios():
    return render_template('prontuarios.html')



@app.route('/cadastro-servicos')
def cadastro_servicos():
    return render_template('cadastro-servicos.html')



@app.route('/historico-de-servicos')
def historico_de_servicos():
    return render_template('historico-de-servicos.html')


@app.route('/perfil-veterinario')
def perfil_veterinario():
    return render_template('perfil-veterinario.html')


if __name__ == '__main__' :
    app.run(debug=True)