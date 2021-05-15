class No {
    constructor(pai = null, valor1 = null, valor2 = null, anterior = null, proximo = null) {
        this.pai = pai
        this.valor1 = valor1
        this.valor2 = valor2
        this.anterior = anterior
        this.proximo = proximo
    }
}

class lista {

    constructor(head, tail) {
        this.head = null;
        this.valor1 = null;
    }

    inserePrimeiro(valor1, valor2, pai) {
        novo_no = new No(pai, valor1, valor2, null, null)
        if (this.head == null) {
            this.tail = novo_no;
            this.head = novo_no;
        } else {
            novo_no.proximo = this.head;
            this.head.anterior = novo_no;
            self.head = novo_no;
        }
    }

    insereUltimo(valor1, valor2, pai) {

        novo_no = new No(valor1, valor2, pai);

        if (this.head === null) {
            this.head = novo_no;
        } else {
            this.tail.proximo = novo_no;
            novo_no.anterior = this.tail;
        }
        this.tail = novo_no;
    }

    deletaPrimeiro(this) {
        if (this.head === null) {
            return null;
        } else {
            no = this.head;
            this.head = this.head.proximo;
            if (this.head != null) {
                this.head.anterior = null;
            } else {
                this.tail = null;
            }
            return no;
        }
    }

    deletaUltimo(this) {
        if (this.tail === null) {
            return null;
        } else {
            no = this.tail;
            this.tail = this.tail.anterior;
            if (this.tail != null) {
                this.tail.proximo == null;
            } else {
                this.head == null;
            }
            return no;
        }
    }

    vazio(this) {
        if (this.head = null) {
            return true;
        } else {
            return false;
        }
    }

    exibeLista(this) {
        aux == this.head;
        str = []
        while (aux != null) {
            temp = [];
            temp.push(aux.valor1);
            temp.push(aux.valor2);
            str.push(temp);
            aux = aux.proximo;
        }

        return str;
    }

    exibeCaminho(this) {
        atual = this.tail;
        caminho = [];
        while (atual.pai != null) {
            caminho.push(atual.valor1);
            atual = atual.pai;
        }
        caminho.push(atual.valor1);
        //Inverter a lista
        caminho = caminho.reverse();
        return caminho;
    }

    exibeCaminho1(this, valor) {

        atual = this.head;
        while (atual.valor1 != valor) {
            atual = atual.proximo;
        }

        caminho = [];
        atual = atual.pai;
        while (atual.pai != null) {
            caminho.push(atual.valor1);
            atual = atual.pai;
        }
        caminho.push(atual.valor1);
        return caminho;
    }

    primeiro(this) {
        return this.head;
    }

    ultimo(this) {
        return this.tail;
    }

}


class busca {

    sucessor(this, x, y) {
        f = []

        // direita
        if ((y + 1) < 14) {
            if (mapa[x][y + 1] != "1") {
                linha = [];
                linha.push(x);
                linha.push(y + 1);
                f.push(linha);
            }
        }

        // esquerda
        if ((y - 1) >= 0) {
            if (mapa[x][y - 1] != "1") {
                linha = [];
                linha.push(x);
                linha.push(y - 1);
                f.push(linha);
            }
        }

        // acima
        if ((x + 1) < 15) {
            if (mapa[x + 1][y] != "1") {
                linha = [];
                linha.push(x + 1);
                linha.push(y);
                f.push(linha);
            }
        }

        // abaixo
        if ((x - 1) >= 0) {
            if (mapa[x - 1][y] != "1") {
                linha = [];
                linha.push(x - 1);
                linha.push(y);
                f.push(linha);
            }
        }

        return f;
    }

    amplitude(this, inicio, fim) {
        caminho = [];

        l1 = lista;

        l2 = lista;

        l1.insereUltimo(inicio, 0, null);
        l2.insereUltimo(inicio, 0, null)

        visitado = [];
        linha = [];
        linha.push(inicio);
        linha.push(0);
        visitado.push(linha);

        while (l1.vazio() != null) {
            atual = l1.deletaPrimeiro();
            if (atual = null) {
                break
            } else {
                filhos = [];
                filhos = this.sucessor(atual.valor1[0], atual.valor1[1]);
            } for (i in range(length(filhos))) {
                novo = filhos[i];
                flag = true;
            } for (j in range(length(visitado))) {
                if (visitado[j][0] == novo) {
                    if (visitado[j][1] <= (atual.valor2 + 1)) {
                        flag = false;
                    }
                    else {
                        visitado[j][1] = atual.valor2 + 1;
                    }
                    break
                }

            }

            if (flag = l1.insereUltimo(novo, atual.valor2 + 1, atual)); {
                if (flag = l2.insereUltimo(novo, atual.valor2 + 1, atual));
                linha = [];
                linha.push(novo);
                linha.push(atual.valor2 + 1);
                visitado.push(linha);

                if (novo == fim) {
                    caminho += l2.exibeCaminho();
                    print("Arvore de busca: \n", l2.exibeLista());
                    return (caminho);
                }
            }

        } return ("Caminho nao encontrado!");

    }
    profundidade(this, inicio, fim) {
        caminho = [];

        l1 = lista;

        l2 = lista;

        l1.insereUltimo(inicio, 0, null);
        l2.insereUltimo(inicio, 0, null)

        visitado = [];
        linha = [];
        linha.push(inicio);
        linha.push(0);
        visitado.push(linha);

        while (l1.vazio() != null) {

            atual = l1.deletaUltimo();
            if (atual = null) {
                break
            } else {
                filhos = [];
                filhos = this.sucessor(atual.valor1[0], atual.valor1[1]);
            } for (i in range(length(filhos))) {
                novo = filhos[i];
                flag = true;

                for (j in range(length(visitado))) {
                    if (visitado[j][0] == novo) {
                        if (visitado[j][1] <= atual.valor2 + 1) {
                            flag = false;
                        } else {
                            visitado[j][1] = atual.valor2 + 1;
                        }
                        break
                    }
                }
                if (flag = l1.insereUltimo(novo, atual.valor2 + 1, atual)) {
                    if (flag = l2.insereUltimo(novo, atual.valor2 + 1, atual)) {
                        linha = [];
                        linha.push(novo);
                        linha.push(atual.valor2 + 1);
                        visitado.push(linha);

                        if (novo == fim) {
                            aminho += l2.exibeCaminho();
                            return (caminho)
                        }
                    }
                }
            }


        } return ("Caminho nao encontrado")

    }
}

mapa = [
    [],
    ["0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0"],
    ["3", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "1", "1", "1", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0"],
    ["0", "0", "1", "1", "1", "0", "0", "2", "0", "0", "1", "1", "1", "0", "0"]
]

sol = busca()
caminho = []

origem = [14, 7]
destino = [5, 0]


caminho = sol.amplitude(origem, destino)
console.log("Amplitude.......: ", caminho)

/*
********************************************************************
        PROBLEMA 1: MAPA DA ROMÊNIA
********************************************************************
*/

nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
    "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
    "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
    "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
    "URZICENI", "VASLUI", "ZERIND"]

// ORDEM DECRESCENTE

grafo = [
    ["ZERIND", "TIMISOARA", "SIBIU"],                 //0
    ["URZICENI", "PITESTI", "GIORGIU", "FAGARAS"],
    ["RIMNICU VILCEA", "PITESTI", "DOBRETA"],
    ["MEHADIA", "CRAIOVA"],
    ["HIRSOVA"],
    ["SIBIU", "BUCARESTE"],
    ["BUCARESTE"],
    ["URZICENI", "EFORIE"],
    ["VASLUI", "NEAMT"],
    ["TIMISOARA", "MEHADIA"],
    ["LUGOJ", "DOBRETA"],
    ["IASI"],
    ["ZERIND", "SIBIU"],
    ["RIMNICU VILCEA", "CRAIOVA", "BUCARESTE"],
    ["SIBIU", "PITESTI", "CRAIOVA"],
    ["RIMNICU VILCEA", "ORADEA", "FAGARAS", "ARAD"],
    ["LUGOJ", "ARAD"],
    ["VASLUI", "HIRSOVA", "BUCARESTE"],
    ["URZICENI", "IASI"],
    ["ORADEA", "ARAD"]
]