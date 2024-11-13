
function editarServiço(button) {

  var row = button.parentNode.parentNode;


  // pega os valores das celulas da linha //

  var data=row.cells[0].textContent;
  var valor =row.cells[1].textContent;
  var servico = row.cells[2].textContent;
  var pet = row.cells[3].textContent;
  var veterinario = row.cells[4].textContent;

// pro usuario editar os valores//

var novaData = prompt("digite a nova dta:",data);
var novoValor = prompt("digite o novo valor:",valor);
var novoServiço= prompt("digite o novo serviço::",servico);
var novoPet = prompt("digite o novo nome do pet:",pet);
var novoVeterinario = prompt("digite o novo veterinario:",veterinario);

// atualiza os val na tabela //
if(novaData && novoValor && novoServiço && novaPet && novoVeterinario) {
    row.cells[0].textContent = novaData;
    row.cells[1].textContent = novoValor;
    row.cells[2].textContent = novoServiço;
    row.cells[3].textContent = novoPet;
    row.cells[4].textContent = novoVeterinario;
}

}


// funçao pra exlcuir a linha na tab//

function excluirServiço(button) {
     
    var confirmacao = confirm("Tem certeza que deseja excluir este serviço?");

    if(confirmacao){
        var row =button.parentNode.parentNode;
        
        row.remove();
    }
}