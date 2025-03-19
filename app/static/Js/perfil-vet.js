function habilitarEdicao(campo) {
    var campoInput =document.getElementById(campo);
    var botaoEditar =campoInput.nextElementSibling; //pega o botao editar //

    //habilita o campo de entrada para a ediçao //

    campoInput.disabled = false;
    document.getElementById("salvar").disabled = false;
     //troca o texto do botão pra salvar//

     botaoEditar.innerText = "SALVAR";

         //alterar o comportamento do botão pra salvar apos editar//
         botaoEditar.onclick = function() {
            document.getElementById("form-perfil").submit();
        };
}

function salvarEdicao(campo) {
    var campoInput = document.getElementById(campo);
    var botaoEditar =campoInput.nextElementSiblig; //pega o botao salvar//
    
    //desabilita o campo apos salvar//
    
    campoInput.disabled = true;

     //Troca o texto do botão de volta para "editar"//
 
     botaoEditar.innerText = "EDITAR";

     //Alterar o comportamento do botao para"editar" novamente //

     botaoEditar.setAttribute("onclick", "habilitarEdicao("+ campo +")");

}