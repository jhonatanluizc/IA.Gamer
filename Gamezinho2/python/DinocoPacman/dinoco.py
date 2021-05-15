import math


class No(object):
    def __init__(self, pai=None, x=None, y=None, nivel=None, custo=None, anterior=None, proximo=None):
        self.pai       = pai
        self.x         = x
        self.y         = y
        self.nivel     = nivel
        self.custo     = custo
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, x, y, nivel, custo, p):
        novo_no = No(p, x, y, nivel, custo, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, x, y, nivel, custo, p):

        novo_no = No(p, x, y, nivel, custo, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

    def inserePos_X(self, x, y, nivel, custo, p):

        if self.head is None:
            self.inserePrimeiro(x, y, nivel, custo, p)
        else:
            atual = self.head
            while atual.custo < custo:
                atual = atual.proximo
                if atual is None: break

            if atual == self.head:
                self.inserePrimeiro(x, y, nivel, custo, p)
            else:
                if atual is None:
                    self.insereUltimo(x, y, nivel, custo, p)
                else:
                    novo_no = No(p, x, y, nivel, custo, None, None)
                    aux = atual.anterior
                    aux.proximo = novo_no
                    novo_no.anterior = aux
                    atual.anterior = novo_no
                    novo_no.proximo = atual

    # REMOVE NO INÍCIO DA LISTA
    def deletaPrimeiro(self):
        if self.head is None:
            return None
        else:
            no = self.head
            self.head = self.head.proximo
            if self.head is not None:
                self.head.anterior = None
            else:
                self.tail = None
            return no

    # REMOVE NO FIM DA LISTA
    def deletaUltimo(self):
        if self.tail is None:
            return None
        else:
            no = self.tail
            self.tail = self.tail.anterior
            if self.tail is not None:
                self.tail.proximo = None
            else:
                self.head = None
            return no

    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
    
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            linha = []
            linha.append(atual.x)
            linha.append(atual.y)
            caminho.append(linha)
            atual = atual.pai


        linha = []
        linha.append(atual.x)
        linha.append(atual.y)
        caminho.append(linha)
        caminho = caminho[::-1]
        caminho.remove(caminho[0])
        return caminho

    def exibeCaminho1(self, no):
                
        atual = self.head
        coordenadas = []
        coordenadas.append(atual.x)
        coordenadas.append(atual.y)
        while coordenadas != no:
            atual = atual.proximo
            coordenadas = []
            coordenadas.append(atual.x)
            coordenadas.append(atual.y)

        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            linha = []
            linha.append(atual.x)
            linha.append(atual.y)
            caminho.append(linha)
            atual = atual.pai

        linha = []
        linha.append(atual.x)
        linha.append(atual.y)
        caminho.append(linha)
        return caminho


    def exibeCaminho2(self, coordenadas, custo):

        atual = self.tail

        linha = []
        linha.append(atual.x)
        linha.append(atual.y)

        while linha != coordenadas or atual.custo != custo:
            atual = atual.anterior
            linha = []
            linha.append(atual.x)
            linha.append(atual.y)

        caminho = []
        while atual.pai is not None:
            linha = []
            linha.append(atual.x)
            linha.append(atual.y)
            caminho.append(linha)
            atual = atual.pai
        linha = []
        linha.append(atual.x)
        linha.append(atual.y)
        caminho.append(linha)
        return caminho

    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):



    def sucessor(self,x,y,character):
        pos = No(None,x,y,0,None,None)
        acao = []
        block = None
        if(character == 'G'):
            block = 'C'

        # ir para direita
        if(pos.x+1 < 10):
            xx = pos.x + 1
            yy = pos.y
            if (mapa[xx][yy] != 1 and mapa[xx][yy] != 'G' and mapa[xx][yy] != block):
                posicao = []
                posicao.append(xx)
                posicao.append(yy)
                custo = []
                custo.append(posicao)
                custo.append(3)
                acao.append(custo)

        # ir para esquerda
        if(pos.x-1 >= 0):
            xx = pos.x - 1
            yy = pos.y
            if (mapa[xx][yy] != 1 and mapa[xx][yy] != 'G' and mapa[xx][yy] != block):
                posicao = []
                posicao.append(xx)
                posicao.append(yy)
                custo = []
                custo.append(posicao)
                custo.append(2)
                acao.append(custo)

        # ir para cima
        if(pos.y+1 < 11):
            xx = pos.x
            yy = pos.y + 1
            if (mapa[xx][yy] != 1 and mapa[xx][yy] != 'G' and mapa[xx][yy] != block):
                 posicao = []
                 posicao.append(xx)
                 posicao.append(yy)
                 custo = []
                 custo.append(posicao)
                 custo.append(1)
                 acao.append(custo)

        #ir para baixo
        if(pos.y-1 >= 0):
            xx = pos.x
            yy = pos.y - 1
            if (mapa[xx][yy] != 1 and mapa[xx][yy] != 'G' and mapa[xx][yy] != block):
                posicao = []
                posicao.append(xx)
                posicao.append(yy)
                custo = []
                custo.append(posicao)
                custo.append(2)
                acao.append(custo)

        return acao

    def heuristica(self, p1,p2):
        return math.fabs(p1[0]-p2[0])+math.fabs(p1[1]-p2[1])

    def amplitude(self, inicio, fim, character):

        # manipular a FILA para a busca
        l1 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio[0],inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0],inicio[1], 0, 0, None)

        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        #ite = 0
        while l1.vazio() is not None:
            # remove o primeiro da fila
            #ite += 1
            #print("\n\n**** Iteração = ",ite)
            #print("Nós já visitados: ", visitado)
            atual = l1.deletaPrimeiro()
            #print("Nó removido da FILA: ", atual.valor1)
            if atual is None: break
            #ind = nos.index(atual.v)
            # varre todos as conexões dentro do grafo a partir de atual
            acao = self.sucessor(atual.x,atual.y, character)
            for i in range(len(acao)):
                novo = acao[i][0]
                #print("\tFilho de atual: ",novo)
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo[0],novo[1], atual.nivel + 1, 0, atual)
                    l2.insereUltimo(novo[0],novo[1], atual.nivel + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = l2.exibeCaminho()
                        return caminho

        return 'caminho não encontrado'

    def profundidade(self, inicio, fim, character):

        # manipular a FILA para a busca
        l1 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)

        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        # ite = 0
        while l1.vazio() is not None:
            # remove o primeiro da fila
            # ite += 1
            # print("\n\n**** Iteração = ",ite)
            # print("Nós já visitados: ", visitado)
            # print("Conteúdo da lista: ", l1.exibe Lista())
            atual = l1.deletaUltimo()
            # print("Nó removido da FILA: ", atual.valor1)
            if atual is None: break
            # ind = nos.index(atual.v)
            # varre todos as conexões dentro do grafo a partir de atual
            acao = self.sucessor(atual.x, atual.y, character)
            for i in range(len(acao)-1,-1,-1):
                novo = acao[i][0]
                # print("\tFilho de atual: ",novo)
                flag = True  # pressuponho que não foi visitado

                # para cada conexão verifica se já foi visitado
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= (atual.nivel + 1):
                            flag = False
                        else:
                            visitado[j][1] = atual.nivel + 1
                        break

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)
                    l2.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel + 1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = l2.exibeCaminho()
                        return caminho

        return "caminho não encontrado"

    def profundidade_limitada(self, inicio, fim, limite, character):

        # manipular a FILA para a busca
        l1 = lista()
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)

        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        # ite = 0
        while l1.vazio() is not None:
            # remove o primeiro da fila
            # ite += 1
            # print("\n\n**** Iteração = ",ite)
            # print("Nós já visitados: ", visitado)
            # print("Conteúdo da lista: ", l1.exibe Lista())
            atual = l1.deletaUltimo()

            if atual is None: break
            # print("Nó removido da FILA: ", atual.valor1)
            if (atual.nivel) < limite:
                # ind = nos.index(atual.v)
                # varre todos as conexões dentro do grafo a partir de atual
                acao = self.sucessor(atual.x, atual.y, character)
                for i in range(len(acao)-1,-1,-1):
                    novo = acao[i][0]
                    # print("\tFilho de atual: ",novo)
                    flag = True  # pressuponho que não foi visitado

                    # para cada conexão verifica se já foi visitado
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] <= (atual.nivel + 1):
                                flag = False
                            else:
                                visitado[j][1] = atual.nivel + 1
                            break

                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)
                        l2.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)

                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel + 1)
                        visitado.append(linha)

                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = l2.exibeCaminho()
                            return caminho

        return "caminho não encontrado"

    def aprofundamento_iterativo(self, inicio, fim, character):
        for limite in range(len(mapa)*len(mapa[0])):
            caminho = []

            # manipular a FILA para a busca
            l1 = lista()

            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()

            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
            l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)

            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)

            while l1.vazio() is not None:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                if atual is None: break

                if (atual.nivel) < limite:
                    acao = self.sucessor(atual.x,atual.y, character)

                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(acao)):

                        novo = acao[i][0]
                        # print("\tFilho de atual: ",novo)
                        flag = True  # pressuponho que não foi visitado

                        # para cada conexão verifica se já foi visitado
                        for j in range(len(visitado)):
                            if visitado[j][0] == novo:
                                if visitado[j][1] <= (atual.nivel + 1):
                                    flag = False
                                else:
                                    visitado[j][1] = atual.nivel + 1
                                break

                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)
                            l2.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)

                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel + 1)
                            visitado.append(linha)

                            # verifica se é o objetivo
                            if novo == fim:
                                caminho += l2.exibeCaminho()
                                return caminho


        return "caminho não encontrado"

    def bidirecional(self, inicio, fim, character):

        # listas para a busca a partir da origem - busca 1
        l1 = lista()  # busca na FILA
        l2 = lista()  # cópia da árvore completa

        # listas para a busca a partir da destino -  busca 2
        l3 = lista()  # busca na FILA
        l4 = lista()  # cópia da árvore completa

        # cria estrutura para controle de nós visitados
        visitado = []

        l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(1)
        visitado.append(linha)

        l3.insereUltimo(fim[0], fim[1], 0, 0, None)
        l4.insereUltimo(fim[0], fim[1], 0, 0, None)
        linha = []
        linha.append(fim)
        linha.append(2)
        visitado.append(linha)

        while True:

            # EXECUÇÃO DO PRIMEIRO AMPLITUDE - BUSCA 1
            flag1 = True
            while flag1:
                atual = l1.deletaPrimeiro()
                acao = self.sucessor(atual.x,atual.y, character)
                for i in range(len(acao)):
                    novo = acao[i][0]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] == 1:  # visitado na mesma árvore
                                flag2 = False
                            else:  # visitado na outra árvore
                                flag3 = True
                            break
                    # for j

                    if flag2:
                        l1.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)
                        l2.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)

                        if flag3:
                            caminho = l2.exibeCaminho()
                            # caminho = caminho[::-1]
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(1)
                            visitado.append(linha)
                        # if flag3
                    # if flag2
                # for i

                if (l1.vazio() != True):
                    aux = l1.primeiro()
                    if aux.nivel == atual.nivel:
                        flag1 = True
                    else:
                        flag1 = False

                        # EXECUÇÃO DO SEGUNDO AMPLITUDE - BUSCA 2
            flag1 = True
            while flag1:
                atual = l3.deletaPrimeiro()
                if atual == None:
                    break
                acao = self.sucessor(atual.x,atual.y, character)
                for i in range(len(acao)):
                    novo = acao[i][0]
                    flag2 = True
                    flag3 = False
                    for j in range(len(visitado)):
                        if visitado[j][0] == novo:
                            if visitado[j][1] == 2:
                                flag2 = False
                            else:
                                flag3 = True
                            break
                    if flag2:
                        l3.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)
                        l4.insereUltimo(novo[0], novo[1], atual.nivel + 1, 0, atual)

                        if flag3:
                            caminho = l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            caminho = caminho[::-1]
                            return caminho
                        else:
                            linha = []
                            linha.append(novo)
                            linha.append(2)
                            visitado.append(linha)

                if (l3.vazio() != True):
                    aux = l3.primeiro()
                    if (atual.nivel == aux.nivel):
                        flag1 = True
                    else:
                        flag1 = False

    def custo_uniforme(self, inicio, fim, character):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()

            coordenadas = []
            coordenadas.append(atual.x)
            coordenadas.append(atual.y)

            if coordenadas == fim:
                caminho = l2.exibeCaminho2(coordenadas, atual.custo)
                return caminho[::-1], atual.custo

            acao = self.sucessor(atual.x,atual.y, character)
            for i in range(len(acao)):
                novo = acao[i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.custo + acao[i][1]
                v1 = v2

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v1:
                            flag1 = False
                        else:
                            visitado[j][1] = v1
                            flag2 = False
                        break
                if flag1:
                    l1.inserePos_X(novo[0], novo[1], v1, v1, atual)
                    l2.inserePos_X(novo[0], novo[1], v1, v1, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"

    def greedy(self, inicio, fim, character):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()

            coordenadas = []
            coordenadas.append(atual.x)
            coordenadas.append(atual.y)

            if coordenadas == fim:
                caminho = l2.exibeCaminho2(coordenadas, atual.custo)
                return caminho, atual.custo

            acao = self.sucessor(atual.x,atual.y, character)
            for i in range(len(acao)):
                novo = acao[i][0]

                # HEURÍSTICA DO NÓ ATUAL ATÉ O OBJETIVO
                v2 = atual.custo + acao[i][1]
                v1 = self.heuristica(novo, fim)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1] = v1
                        break

                if flag1:
                    l1.inserePos_X(novo[0], novo[1], 0, v2, atual)
                    l2.inserePos_X(novo[0], novo[1], 0, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"

    def a_estrela(self, inicio, fim, character):

        l1 = lista()
        l2 = lista()
        visitado = []

        l1.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        l2.insereUltimo(inicio[0], inicio[1], 0, 0, None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() is not None:
            atual = l1.deletaPrimeiro()

            coordenadas = []
            coordenadas.append(atual.x)
            coordenadas.append(atual.y)
            if coordenadas == fim:
                caminho = l2.exibeCaminho2(coordenadas, atual.custo)
                return caminho, atual.custo

            acao = self.sucessor(atual.x,atual.y, character)
            for i in range(len(acao)):
                novo = acao[i][0]

                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.nivel + acao[i][1]
                v1 = v2 + self.heuristica(novo,fim)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0] == novo:
                        if visitado[j][1] <= v1:
                            flag1 = False
                        else:
                            flag2 = False
                            visitado[j][1] = v1
                        break

                if flag1:
                    l1.inserePos_X(novo[0], novo[1], v2, v1, atual)
                    l2.inserePos_X(novo[0], novo[1], v2, v1, atual)
                    if flag2:
                        linha = []
                        linha.append(novo)
                        linha.append(v1)
                        visitado.append(linha)

        return "Caminho não encontrado"

class ambiente(object):
    '''Retorna a lista de posições dos Fantamas do jogo no mapa'''
    def getMapPositionGhosts(self):
        list = []
        x = 0
        y = 0
        for position_x in mapa:
            for position_y in position_x:
                if(position_y == "G"):
                    list.append([x, y, position_y])
                y+=1
            x+=1
            y=0
        return list

    '''Retorna a posição do Pacman no Mapa'''
    def getMapPositionPacman(self):
        coordenada = []
        x = 0
        y = 0
        for position_x in mapa:
            for position_y in position_x:
                if(position_y == "P"):
                    coordenada.append(x)
                    coordenada.append(y)
                    return coordenada
                y+=1
            x+=1
            y=0

    '''Retorna a posição do Objetivo no Mapa'''
    def getMapPositionFood(self):
        coordenada = []
        x = 0
        y = 0
        for position_x in mapa:
            for position_y in position_x:
                if (position_y == "C"):
                    coordenada.append(x)
                    coordenada.append(y)
                    return coordenada
                y += 1
            x += 1
            y = 0

    def getRoutes(self, PacmanMove, GhostsMove):
        caminhos = []
        sol = busca()
        pacman = self.getMapPositionPacman()

        if(PacmanMove == 'amplitude'):
            #Rota do Pacman
            caminho = sol.amplitude(pacman, self.getMapPositionFood(), 'P')
            caminhos.append([caminho, [pacman[0],pacman[1],'P']])

        if(GhostsMove == 'amplitude'):
            #Rotas dos Fantasmas
            for i in self.getMapPositionGhosts():
                ghost = [i[0], i[1]]
                caminho = []
                caminho = sol.amplitude(ghost, pacman, 'G')
                caminhos.append([caminho,i])

        return caminhos

    def walk(self, routes):
        for caminho in routes:
            if(caminho[0] != None and caminho[0] == 'caminho não encontrado'):
                mapa[caminho[1][0]][caminho[1][1]] = 0
                if (caminho[1][2] == 'P' and mapa[caminho[0][0][0]][caminho[0][0][1]] == 'G'):
                    mapa[caminho[0][0][0]][caminho[0][0][1]] = 'G'
                    print('Game Over')
                    return True
                elif(caminho[1][2] == 'G' and mapa[caminho[0][0][0]][caminho[0][0][1]] == 'P'):
                    mapa[caminho[0][0][0]][caminho[0][0][1]] = 'G'
                    print('Game Over')
                    return True
                elif(caminho[1][2] == 'P' and mapa[caminho[0][0][0]][caminho[0][0][1]] == 'C'):
                    mapa[caminho[0][0][0]][caminho[0][0][1]] = 'P'
                    print('Game Win')
                    return True
                else:
                    mapa[caminho[0][0][0]][caminho[0][0][1]] = caminho[1][2]
        return False

mapa =  [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,1,0,0,0,"G",0,0,0,0,1,0,0,0,0,1],
            [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
            [1,"C",1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
            [1,"G",0,0,0,1,0,0,0,0,"P",0,0,0,1,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

'''sol = busca()
caminho = []

origem  = [7,1]
destino = [1,9]'''

teste = ambiente()

while True:
    if(teste.walk(teste.getRoutes('amplitude', 'amplitude'))):
        break
'''
caminho = sol.aprofundamento_iterativo(origem,destino)
print("\nAprof. Iterativo...:",caminho)

caminho = []
caminho, custo = sol.a_estrela(origem,destino)
print("\nA estrela: ",caminho[::-1],"\ncusto do caminho: ",custo)

caminho=[]
caminho, custo = sol.greedy(origem,destino)
print("\nGreedy: ",caminho[::-1],"\ncusto do caminho: ",custo)

caminho = []
caminho = sol.custo_uniforme(origem,destino)
print("\nCusto Uniforme.......: ",caminho[0],"\nCusto: ",caminho[1])

caminho = []
caminho = sol.bidirecional(origem,destino)
print("\nBidirecional.......: ",caminho)

caminho = []
caminho = sol.profundidade(origem,destino)
print("\nProfundidade.......: ",caminho)

caminho = []
caminho = sol.profundidade_limitada(origem,destino,15)
print("\nProfundidade.......: ",caminho)'''