Game = {

    /// :: Mapa do jogo. P = player, E = inimigo,  G = chegada
    Mapa: [
        ['P', 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        ['E', 1, 0, 0, 1, 0, 0, 'G']
    ],

    /// :: Inicia jogo.
    Start: function () {

        var x = 0;
        var pCasas = [];
        var total_casas = [];

        var numero_colunas = 8;
        var numero_linhas = 8;
        var numero_casas = numero_colunas * numero_linhas;

        var p1ActualHouse = 0;
        var cpuActualHouse = 0;


        var contHouses = 0;
        var turn = true;



        while (x < numero_casas) {
            //console.log("Hey "+x);
            $("#game").append(" <div class='div-casa' id='" + (x + 1) + "'></div> ");
            pCasas.push(0);

            x = x + 1;

            if (x % numero_colunas == 0) {

                total_casas.push(pCasas);
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

            if ($(this).find('img').length > 0) {
                alert("Movimento inválido");

            } else {

                pCasas = new Array(8).fill(0);

                p1ActualHouse = this.id;
                pCasas[newHouse] = 1;

                $('.div-casa[name="p1"]').empty();
                $('.div-casa[name="p1"]').removeAttr("name");
                $(this).attr("name", "p1");
                $(this).append("<img id='player' src='p1.gif' />");

            }
        });


        //Gerenciador de turnos, enquanto na for a vez dele ele nao faz nada, quando for ele desabilita todos os comandos de andar do player

        function BeginGame() {
            (function my_func() {
                if (turn != true) {
                    $('.div-casa').css({
                        "pointer-events": "none"
                        // "pointer-events": ""
                        // "pointer-events": "none"
                    });

                } else {
                    console.log("N é sua vez CPU , restam " + contHouses);

                }
                setTimeout(my_func, 1000);
            })();
        }



    },

    /// :: Eventos do jogo.
    Init: function () {

        /// :: Todas as iniciações.
        //Game.Start();
        Game.Render();

        /// :: Gera o mapa.
        Game.Algoritmos.UpdateMap();

        $("#mapa").click(function (e) {

            var id_coluna = e.target.id;
            var id_linha = e.target.parentElement.id;

            x = id_coluna.replace("coluna-", "");
            y = id_linha.replace("linha-", "");

            /// :: Verifica se nao é o click do mapa ou o player.
            if (x !== "mapa" && y !== "mapa" && x !== "player") {
                Game.Move('P', x, y);
            }

        });
    },

    /// :: Renderiza a matriz.
    Render: function () {

        /// :: Limpa o mapa.
        $("#mapa").empty();

        /// :: Percorre todas as linhas.
        Game.Mapa.forEach((linhas, y) => {

            /// :: Cria uma div.
            $("#mapa").append("<div id=linha-" + y + ">");

            /// :: Percorre todas as colunas.
            linhas.forEach((value, x) => {

                /// :: Pega o id da linha e da coluna.
                var id_linha = "linha-" + y;
                var id_coluna = "coluna-" + x;

                /// :: Verifica o que deve ser renderizado.
                if (value === "P") {

                    /// :: Adiciona a casa.
                    $("#" + id_linha).append("<div id=" + id_coluna + " class='div-casa' ></div>");

                    /// :: Adiciona o player na casa.
                    $("#" + id_linha).find("#" + id_coluna).append("<img id='player' src='p1.gif' />");

                } else if (value === "E") {

                    /// :: Adiciona a casa.
                    $("#" + id_linha).append("<div id=" + id_coluna + " class='div-casa' ></div>");

                    /// :: Adiciona o enemy na casa.
                    $("#" + id_linha).find("#" + id_coluna).append("<img id='player' src='enemy.gif' />");

                } else if (value === "G") {

                    /// :: Adiciona a casa.
                    $("#" + id_linha).append("<div id=" + id_coluna + " class='div-casa' ></div>");

                    /// :: Adiciona o goal na casa.
                    $("#" + id_linha).find("#" + id_coluna).append("<img id='player' src='goal.gif' />");

                } else if (value === 1) {

                    /// :: Adiciona bloco invalido.
                    $("#" + id_linha).append("<div id=" + id_coluna + " class='div-casa' style='background-color: red;'></div>");
                } else {

                    /// :: Adiciona a valido.
                    $("#" + id_linha).append("<div id=" + id_coluna + " class='div-casa'></div>");
                }

            });

        });

    },

    /// :: Com base no x e y vai movimentar o personagem.
    Move: function (personagem, x, y) {

        /// :: Percorre todas as linhas.
        Game.Mapa.forEach((linhas, yy) => {

            /// :: Percorre todas as colunas.
            linhas.forEach((value, xx) => {

                /// :: Se encontrou o player.
                if (value === personagem)
                    Game.Mapa[yy][xx] = 0;

            })
        })

        Game.Mapa[y][x] = personagem;
        Game.Render();
    },

    /// :: Procura o caminho até o jogador e vai em direção a ele.
    Hunt: function () {

        var pos_jogador = [0, 0];
        var pos_inimigo = [0, 0];

        /// :: Percorre todas as linhas.
        Game.Mapa.forEach((linhas, yy) => {

            /// :: Percorre todas as colunas.
            linhas.forEach((value, xx) => {

                /// :: Se encontrou o player.
                if (value === 'P')
                    pos_jogador = [yy, xx];

                /// :: Se encontrou o inimigo.
                if (value === 'E')
                    pos_inimigo = [yy, xx];

            })
        })

        //console.log(Game.Algoritmos.Amplitude(pos_jogador, pos_inimigo));
        console.log(Game.Algoritmos.Amplitude(pos_inimigo, pos_jogador));

    },

    /// :: Funções para chamar os algoritmos.
    Algoritmos: {

        /// :: Cria uma solução.
        Solucao: new busca(),

        /// :: Atualiza o mapa.
        UpdateMap: function () {
            mapa = Game.Mapa;
        },

        /// :: Amplitude.
        Amplitude: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.amplitude(origem, destino);
        },

        /// :: Profundidade.
        Profundidade: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.profundidade(origem, destino);
        },

        /// :: Profundidade Limitada.
        ProfundidadeLimitada: function (origem, destino, limite) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.profundidade_limitada(origem, destino, limite);
        },

        /// :: Aprofundamento Iterativo.
        AprofundamentoIterativo: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.aprofundamento_iterativo(origem, destino);
        },

        /// :: Bidirecional.
        Bidirecional: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.bidirecional(origem, destino);
        },

        /// :: Custo Uniforme.
        CustoUniforme: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.custo_uniforme(origem, destino);
        },

        /// :: Greedy.
        Greedy: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.greedy(origem, destino);
        },

        /// :: Estrela.
        Estrela: function (origem, destino) {

            ///:: Atualiza o mapa.
            Game.Algoritmos.UpdateMap();
            return Game.Algoritmos.Solucao.a_estrela(origem, destino);
        },
    }
}


Game.Init();