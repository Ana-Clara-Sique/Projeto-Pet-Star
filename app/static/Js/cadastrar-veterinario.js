// Aguardar o carregamento completo do DOM
document.addEventListener("DOMContentLoaded", function () {
    // Adiciona um ouvinte de evento no formulário de cadastro
    const form = document.getElementById('form-cadastro');
    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Impede o envio tradicional do formulário

        // Coleta os dados do formulário
        const nome = document.getElementById('campo-nome').value;
        const login = document.getElementById('campo-login').value;
        const dataNascimento = document.getElementById('campo-data').value;
        const genero = document.querySelector('input[name="genero"]:checked') ? document.querySelector('input[name="genero"]:checked').value : '';
        const email = document.getElementById('campo-email').value;
        const telefone = document.getElementById('campo-telefone').value;
        const formacaoAcademica = document.getElementById('campo-formacao').value;
        const especializacao = document.getElementById('campo-especializacao').value;
        const senha = document.getElementById('campo-senha').value;
        const observacoes = document.querySelector('textarea[name="observacoes"]').value;

        // Cria um objeto com os dados do formulário
        const dados = {
            nome_completo: nome,
            login: login,
            data_nascimento: dataNascimento,
            genero: genero,
            email: email,
            telefone: telefone,
            formacao_academica: formacaoAcademica,
            especializacao: especializacao,
            senha: senha,
            observacoes: observacoes
        };

        // Envia os dados para o servidor via AJAX (fetch)
        fetch('/api/veterinarios', {
            method: 'POST',
            body: JSON.stringify(dados),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())  // Espera a resposta da API
        .then(data => {
            console.log('Sucesso:', data);
            // Exibe uma mensagem de sucesso ou redireciona o usuário após o sucesso
            if (data && data.id) {
                alert('Veterinário cadastrado com sucesso!');
                window.location.href = '/pagina-principal-vet';  // Redireciona para a página principal
            } else {
                alert('Erro ao cadastrar, tente novamente.');
            }
        })
        .catch((error) => {
            console.error('Erro:', error);
            alert('Ocorreu um erro, tente novamente.');
        });
    });
});
