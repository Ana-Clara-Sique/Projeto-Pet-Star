
// abrir menu lateral  //
 document.getElementById('abrir-menu').addEventListener('click',function(e){
   e.preventDefault();
   document.getElementById('menu-lateral').style.right ='0';  //menu abrir   //

 });

// fechar o menu lateral //
  document.getElementById('fechar-menu').addEventListener('click',function(){
    document.getElementById('menu-lateral').style.right ='250px';  // menu fechar//
    
  })





