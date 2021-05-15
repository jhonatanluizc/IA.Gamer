class No {
    constructor(pai, valor1, valor2, anterior, proximo) {
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
        this.tail = null;
    }

    inserePrimeiro(valor1, valor2, pai) {

        var novo_no = new No(pai, valor1, valor2, null, null)

        if (this.head === null) {
            this.tail = novo_no;
            this.head = novo_no;
        } else {
            novo_no.proximo = this.head;
            this.head.anterior = novo_no;
            this.head = novo_no;
        }
    }

    insereUltimo(valor1, valor2, pai) {

        var novo_no = new No(pai, valor1, valor2, null, null);

        if (this.head === null) {
            this.head = novo_no;
        } else {
            this.tail.proximo = novo_no;
            novo_no.anterior = this.tail;
        }
        this.tail = novo_no;
    }

    deletaPrimeiro() {
        if (this.head === null) {
            return null;
        } else {
            var no = this.head;
            this.head = this.head.proximo;
            if (this.head !== null)
                this.head.anterior = null;
            else
                this.tail = null;

            //console.log("---", no.valor1, no.valor2)
            return no;
        }
    }

    deletaUltimo() {
        if (this.tail === null) {
            return null;
        } else {
           var no = this.tail;
            this.tail = this.tail.anterior;
            if (this.tail !== null)
                this.tail.proximo = null;
            else
                this.head = null;

            return no;
        }
    }

    vazio() {
        if (this.head === null)
            return true;
        else
            return false;
    }

    exibeLista() {
        var aux = this.head;
        var str = [];
        while (aux !== null) {
            var temp = [];
            temp.push(aux.valor1);
            temp.push(aux.valor2);
            str.push(temp);
            aux = aux.proximo;
        }
        return str;
    }

    exibeCaminho() {
        var atual = this.tail;
        var caminho = [];
        while (atual.pai !== null) {
            caminho.push(atual.valor1);
            atual = atual.pai;
        }
        caminho.push(atual.valor1);
        // Inverter a lista
        caminho = caminho.reverse();
        return caminho;
    }

    exibeCaminho1(valor) {

        var atual = this.head;
        while (atual.valor1 !== valor) {
            atual = atual.proximo;
        }

        var caminho = [];
        atual = atual.pai;
        while (atual.pai !== null) {
            caminho.push(atual.valor1);
            atual = atual.pai;
        }
        caminho.push(atual.valor1);
        return caminho;
    }

    primeiro() {
        return this.head;
    }

    ultimo() {
        return this.tail;
    }
}

class busca {

    sucessor(x, y) {
        var f = [];
        var linha = [];

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

    amplitude(inicio, fim) {
        caminho = [];

        var l1 = new lista();

        var l2 = new lista();

        l1.insereUltimo(inicio, 0, null);
        l2.insereUltimo(inicio, 0, null)

        var visitado = [];
        var linha = [];
        linha.push(inicio);
        linha.push(0);
        visitado.push(linha);

        var novo = null;
        var flag = true;

        while (l1.vazio() === false) {

            var atual = l1.deletaPrimeiro();
            if (atual === null) break

            //console.log("atual", atual.valor1)

            var filhos = null;
            filhos = this.sucessor(atual.valor1[0], atual.valor1[1]);

            // console.log("filhos", atual.valor1, atual.valor2);            

            for (var i = 0; i < filhos.length; i++) {

                novo = filhos[i];
                // console.log("novo", novo)
                flag = true;

                for (var j = 0; j < visitado.length; j++) {
                    if (visitado[j][0].toString() === novo.toString()) {
                        if (visitado[j][1] <= (atual.valor2 + 1))
                            flag = false;
                        else
                            visitado[j][1] = atual.valor2 + 1;
                        break
                    }
                }
                
                //console.log(flag)
                
                if (flag) {
                    l1.insereUltimo(novo, atual.valor2 + 1, atual);
                    l2.insereUltimo(novo, atual.valor2 + 1, atual);
    
                    linha = [];
                    linha.push(novo);
                    linha.push(atual.valor2 + 1);
                    visitado.push(linha);
    
                    // console.log("novo", novo, "fim", fim)
                    
                    //console.log(novo, fim)
                    
                    if (novo.toString() === fim.toString()) {
                        caminho += l2.exibeCaminho();
                        return (caminho);
                    }
                }
            }
        }

        return ("Caminho nao encontrado!");

    }

}

var mapa = [
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

var sol = new busca()
var caminho = []

var origem = [14, 7]
var destino = [5, 0]


var caminho = sol.amplitude(origem, destino)

console.log("Amplitude.......: ", caminho)


