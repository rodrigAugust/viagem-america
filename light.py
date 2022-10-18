class No(object):
    def __init__(self, pai=None, estado=None, nivel=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.nivel     = nivel
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, st, v1,p):
        novo_no = No(p, st, v1, None, None)
        if self.head == None:
            self.tail = novo_no
            self.head = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
            self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, st, v1, p):

        novo_no = No(p, st, v1, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no

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

    # RETORNA O PRIMEIRO DA LISTA
    def primeiro(self):
        return self.head
    
    # RETORNA O ÚLTIMO DA LISTA
    def ultimo(self):
        return self.tail

    # VERIFICA SE LISTA ESTÁ VAZIA
    def vazio(self):
        if self.head is None:
            return True
        else:
            return False
        
    # EXIBE O CONTEÚDO DA LISTA
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            temp = []
            temp.append(aux.estado)
            temp.append(aux.nivel)
            str.append(temp)
            aux = aux.proximo
        
        return str
    
    # EXIBE O CAMINHO ENCONTRADO
    def exibeCaminho(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        caminho = caminho[::-1]
        return caminho
    
    # EXIBE O CAMINHO ENCONTRADO (BIDIRECIONAL)
    def exibeCaminho1(self,valor):
                
        atual = self.head
        while atual.estado != valor:
            atual = atual.proximo
    
        if atual.pai == None:
            atual= atual
        else: 
            atual = atual.pai

        caminho = []
       
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho

class busca(object):

    # BUSCA EM AMPLITUDE
    def amplitude(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            #if atual is None: break

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel + 1, atual)
                    l2.insereUltimo(novo, atual.nivel + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return "caminho não encontrado"


    # BUSCA EM PROFUNDIDADE
    def profundidade(self, inicio, fim):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            #if atual is None: break

            ind = nos.index(atual.estado)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(grafo[ind])-1,-1,-1):

                novo = grafo[ind][i]
                # pressuponho que não foi visitado
                flag = True

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.nivel+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.nivel+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.nivel+1, atual)
                    l2.insereUltimo(novo, atual.nivel+1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.nivel+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("Fila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho
        return "caminho não encontrado"
    
    
    # BUSCA EM PROFUNDIDADE
    def prof_limitada(self, inicio, fim, limite):

        # manipular a FILA para a busca
        l1 = lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaUltimo()
            
            if atual.nivel < limite:
                ind = nos.index(atual.estado)

                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])-1,-1,-1):
    
                    novo = grafo[ind][i]
                    # pressuponho que não foi visitado
                    flag = True
    
                    # controle de nós repetidos
                    for j in range(len(visitado)):
                        if visitado[j][0]==novo:
                            if visitado[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel+1, atual)
                        l2.insereUltimo(novo, atual.nivel+1, atual)
    
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado.append(linha)
    
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho
        return "caminho não encontrado"
    
    
    # BUSCA EM PROFUNDIDADE
    def aprof_iterativo(self, inicio, fim, l_max):
        
        for limite in range(l_max):

            # manipular a FILA para a busca
            l1 = lista()
    
            # cópia para apresentar o caminho (somente inserção)
            l2 = lista()
    
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,None)
            l2.insereUltimo(inicio,0,None)
    
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
    
            while l1.vazio() == False:
                # remove o primeiro da fila
                atual = l1.deletaUltimo()
                
                if atual.nivel < limite:
                    ind = nos.index(atual.estado)
    
                    # varre todos as conexões dentro do grafo a partir de atual
                    for i in range(len(grafo[ind])-1,-1,-1):
        
                        novo = grafo[ind][i]
                        # pressuponho que não foi visitado
                        flag = True
        
                        # controle de nós repetidos
                        for j in range(len(visitado)):
                            if visitado[j][0]==novo:
                                if visitado[j][1]<=(atual.nivel+1):
                                    flag = False
                                else:
                                    visitado[j][1]=atual.nivel+1
                                break
                        
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo, atual.nivel+1, atual)
                            l2.insereUltimo(novo, atual.nivel+1, atual)
        
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.nivel+1)
                            visitado.append(linha)
        
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("Fila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho
        return "caminho não encontrado"
    
    #BUSCA BIDIRECIONAL
    def bidirecional(self, inicio, fim):
    
        # manipular a FILA para a busca
        l1 = lista()
        l3 = lista()
    
        # cópia para apresentar o caminho (somente inserção)
        l2 = lista()
        l4 = lista()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)
        l3.insereUltimo(fim,0,None)
        l4.insereUltimo(fim,0,None)
    
    
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                if ni!=l1.primeiro().nivel:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
        
                ind = nos.index(atual.estado)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])):
        
                    novo = grafo[ind][i]
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado1)):
                        if visitado1[j][0]==novo:
                            if visitado1[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado1[j][1]=atual.nivel+1
                            break
                    
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo, atual.nivel + 1, atual)
                        l2.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado2)):
                            if visitado2[j][0]==novo:
                                flag = True
                                break
                        
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                if ni!= l3.primeiro().nivel:
                    break
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
        
                ind = nos.index(atual.estado)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for i in range(len(grafo[ind])):
        
                    novo = grafo[ind][i]
                    # pressuponho que não foi visitado
                    flag = True
        
                    # controle de nós repetidos
                    for j in range(len(visitado2)):
                        if visitado2[j][0]==novo:
                            if visitado2[j][1]<=(atual.nivel+1):
                                flag = False
                            else:
                                visitado2[j][1]=atual.nivel+1
                            break
                        
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo, atual.nivel + 1, atual)
                        l4.insereUltimo(novo, atual.nivel + 1, atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.nivel+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = False
                        for j in range(len(visitado1)):
                            if visitado1[j][0]==novo:
                                flag = True
                                break
                            
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return "caminho não encontrado"
 
"""
********************************************************************
                     PROBLEMA: MAPA DA ROMÊNIA
********************************************************************
"""

nos = ["ARGENTINA", "BOLIVIA", "BRASIL", "CANADA", "CHILE", "COLOMBIA", "COSTA RICA", "CUBA", "REPUPLICA DOMINICANA", "EQUADOR",
"GUIANA FRANCESA", "GROELANDIA", "GUATEMALA", "JAMAICA", "MEXICO", "NICARAGUA", "PERU", "PARAGUAI", "ESTADOS UNIDOS", "URUGUAI", "VENEZUELA"]
#
grafo = [
    #argentina
    ["BRASIL", "CHILE", "PARAGUAI", "URUGUAI"],
    #bolivia
    ["COLOMBIA", "PERU", "PARAGUAI"],
    #brasil
    ["ARGENTINA", "COLOMBIA", "ESTADOS UNIDOS", "NICARAGUA", "VENEZUELA"],
    #canada
    ["ESTADOS UNIDOS", "GROELANDIA", "MEXICO", "NICARAGUA"],
    #chile
    ["ARGENTINA", "COLOMBIA", "PARAGUAI", "URUGUAI"],
    #colombia
    ["BOLIVIA", "BRASIL", "CHILE", "COSTA RICA", "EQUADOR", "NICARAGUA"],
    #costa rica
    ["COLOMBIA", "GUATEMALA", "MEXICO"],
    #cuba
    ["GUATEMALA", "JAMAICA", "NICARAGUA"],
    #republica dominicana
    ["ESTADOS UNIDOS", "GUIANA FRANCESA", "JAMAICA", "VENEZUELA"],
    #equador
    ["COLOMBIA", "PERU"],
    #guiana francesa
    ["REPUPLICA DOMINICANA", "VENEZUELA"],
    #groelandia
    ["CANADA", "ESTADOS UNIDOS"],
    #guatemala
    ["COSTA RICA", "CUBA", "ESTADOS UNIDOS", "NICARAGUA"],
    #jamaica
    ["CUBA", "REPUPLICA DOMINICANA", "VENEZUELA"],
    #mexico
    ["CANADA", "COLOMBIA", "ESTADOS UNIDOS", "GUATEMALA"],
    #nicaragua
    ["BRASIL", "CANADA", "COLOMBIA", "CUBA", "ESTADOS UNIDOS", "GUATEMALA", "VENEZUELA"],
    #peru
    ["BOLIVIA", "EQUADOR"],
    #paraguai
    ["ARGENTINA", "BOLIVIA", "CHILE"],
    #estados unidoos
    ["BOLIVIA", "BRASIL", "CANADA", "GROELANDIA", "MEXICO", "NICARAGUA"],
    #uruguai
    ["ARGENTINA", "CHILE"],
    #venezuela
    ["BRASIL", "REPUPLICA DOMINICANA", "GUIANA FRANCESA", "JAMAICA", "NICARAGUA"]
    ]

# PROGRAMA PRINCIPAL

lig = busca()
caminho = []