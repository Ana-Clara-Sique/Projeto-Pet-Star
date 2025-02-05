from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from models import Veterinario, engine

# Criar a sessão do banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Instanciar o app Flask
app = Flask(__name__)

@app.route('/cadastrar-veterinario', methods=['GET', 'POST'])
def cadastrar_veterinario():
    if request.method == 'POST':
        # Receber os dados do formulário
        nome_completo = request.form['campo-nome']
        data_nascimento = request.form['campo-data']
        genero = request.form['genero']
        email = request.form['campo-email']
        telefone = request.form['campo-telefone']
        formacao_academica = request.form['campo-formacao']
        especializacao = request.form['campo-especializacao']
        senha = request.form['campo-senha']
        endereco = request.form['campo-endereco']
        observacoes = request.form['observacoes']

        # Criar um novo objeto Veterinário
        novo_veterinario = Veterinario(
            nome_completo=nome_completo,
            data_nascimento=data_nascimento,
            genero=genero,
            email=email,
            telefone=telefone,
            formacao_academica=formacao_academica,
            especializacao=especializacao,
            senha=senha,
            endereco=endereco,
            observacoes=observacoes
        )

        # Adicionar e salvar no banco de dados
        session.add(novo_veterinario)
        session.commit()

        return redirect(url_for('index'))  # Redireciona para a página inicial após salvar

    return render_template('cadastrar-veterinario.html')

if __name__ == '__main__':
    app.run(debug=True)
