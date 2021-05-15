var x = 0;
var pCasas = [];

var numero_colunas = 8;
var numero_linhas = 8;
var numero_casas = numero_colunas * numero_linhas;

while (x < numero_casas) {
    //console.log("Hey "+x);
    $("#game").append(" <div class='div-casa' id='" + x + "'></div> ");
    pCasas.push(x);
    x = x + 1;
    
    if (x % numero_colunas == 0){

        $("#game").append("<br>");
    }

}

console.log(pCasas);

$('.div-casa').click(function (e) {

    $('.div-casa').empty();
    $(this).append("<img id='player' src='p1.gif' />");

});