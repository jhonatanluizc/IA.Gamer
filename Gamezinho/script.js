Game = {

    RollRemainP1: 0,
    RollRemainCPU: 0,
    PlayerTurn: true,


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
    Roll: function () {

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

                //debugger

                /// :: Base.
                var player_x = 0;
                var player_y = 0;

                /// :: Pega a posição do player
                /// :: Percorre todas as linhas.
                Game.Mapa.forEach((linhas, yy) => {

                    /// :: Percorre todas as colunas.
                    linhas.forEach((value, xx) => {

                        /// :: Se encontrou o player.
                        if (value === 'P') {
                            player_x = xx;
                            player_y = yy;
                        }

                    })
                })

                //debugger

                var totalMovimento = 0;

                if (x > player_x) {
                    totalMovimento = totalMovimento + x - player_x;
                } else {
                    totalMovimento = totalMovimento + player_x - x;
                }

                if (y > player_y) {
                    totalMovimento = totalMovimento + y - player_y;
                } else {
                    totalMovimento = totalMovimento + player_y - y;
                }

                if (totalMovimento === 1) {
                    /// :: Move o personagem.
                    Game.Move('P', x, y);
                }



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
    },

    Turn: function () {

        debugger
        var rolada = roll();

        if (Game.PlayerTurn === true) {

            if (Game.RollRemainP1 > 0) {
                Game.PlayerTurn = true;
                Game.RollRemainP1--;
                console.log(Game.RollRemainP1);
            } else {
                Game.PlayerTurn = false;
                console.log("Não pode");
            }

        }

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


//Game.Start();
Game.Init();
Game.Turn();