document.getElementById("login-form").addEventListener("submit", function(event){
    // Remover o preventDefault, para permitir que o formulário seja enviado para o servidor
    // event.preventDefault(); 

    const camponome = document.getElementById("campo-nome").value;
    const camposenha = document.getElementById("campo-senha").value;
    const erromensagem = document.getElementById("erro-mensagem");

    // Limpar mensagem de erro antes de exibir novas mensagens
    erromensagem.textContent = "";

    // Verificar se os campos estão vazios
    if (camponome == "" || camposenha === "") {
        erromensagem.textContent = "Por favor, preencha todos os campos!";
        return;
    }

   
});
