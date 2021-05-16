var x = 0;
var pCasas = [];
var tCasas = [];

var numero_colunas = 8;
var numero_linhas = 8;
var numero_casas = numero_colunas * numero_linhas;

var p1ActualHouse = 0;
var cpuActualHouse = 0;


var contHouses = 0;
var turn = true;



while (x < numero_casas) {
    //console.log("Hey "+x);
    $("#game").append(" <div class='div-casa' id='" + (x+1) + "'></div> ");
    pCasas.push(0);

    x = x + 1;
    
    if (x % numero_colunas == 0){

        tCasas.push(pCasas);
        $("#game").append("<br>");
        pCasas = [];

    }

}

//$('.div-casa[id="0"]').attr('id','0').append("<img id='player' src='p1.gif' />");
//$('.div-casa[id="1"]').attr('id','0').append("<img id='player' src='enemy.gif' />");
//$('.div-casa[id="'+Math.floor(Math.random() * 63).toString()+'"]').append("<img id='player' src='goal.gif' />");
//roll();

//Gerenciador de movimentos
$('.div-casa').click(function (e) {

    if($(this).find('img').length > 0){        
        alert("Movimento inválido");
       
    }else{

        pCasas = new Array(8).fill(0);

        p1ActualHouse = this.id;
        pCasas[newHouse] = 1;

        $('.div-casa[name="p1"]').empty();
        $('.div-casa[name="p1"]').removeAttr("name");
        $(this).attr("name","p1");
        $(this).append("<img id='player' src='p1.gif' />");

    }    
});


//Gerenciador de turnos, enquanto na for a vez dele ele nao faz nada, quando for ele desabilita todos os comandos de andar do player


function BeginGame(){
    (function my_func() {
        if(turn != true){
            $('.div-casa').css({
                "pointer-events": "none"
                // "pointer-events": ""
                // "pointer-events": "none"
            });

        }else{
            console.log("N é sua vez CPU , restam "+contHouses);
            
        }
        setTimeout( my_func, 1000 );
    })();
}

