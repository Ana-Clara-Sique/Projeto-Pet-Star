document.getElementById("login-form").addEventListener("submit",function(event){
    event.preventDefault();

    const camponome = document.getElementById("campo-nome").value;

    const camposenha = document.getElementById("campo-senha").value;

    const erromensagem = document.getElementById("erro-mensagem");


    erromensagem.textContent = "";


   //definindo usuario e senha ficticios //

   const validcamponome = "VivianClínicageral01";
   const validcamposenha = "senha123";


    if (camponome == "" || camposenha === "" ){
        erromensagem.textContent ="Por favor , preencha todos os campos!";
        return;
    }

    alert("login realizado com sucesso!");

    if(camponome == validcamponome && camposenha ==validcamposenha)
        {
        window.location.href= "pagina-principal-vet.html";
    
    }  else{
        erromensagem.textContent+"Usuario ou senha invalidos!";
    }

    document.getElementById(login-form).requestFullscreen();
});