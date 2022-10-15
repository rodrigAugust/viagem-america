import random

class No(object):
    def __init__(self, pai=None, estado=None, valor1=None, valor2=None, anterior=None, proximo=None):
        self.pai       = pai
        self.estado    = estado
        self.valor1    = valor1        # valor do nó na árvore
        self.valor2    = valor2        # custo do caminho até o nó atual
        self.anterior  = anterior
        self.proximo   = proximo
    
class lista(object):
    head = None
    tail = None

    # INSERE NO INÍCIO DA LISTA
    def inserePrimeiro(self, s, v1, v2, p):
        novo_no = No(p, s, v1, v2, None, None)
        if self.head == None:
            self.tail = novo_no
        else:
            novo_no.proximo = self.head
            self.head.anterior = novo_no
        self.head = novo_no

    # INSERE NO FIM DA LISTA
    def insereUltimo(self, s, v1, v2, p):

        novo_no = No(p, s, v1, v2, None, None)

        if self.head is None:
            self.head = novo_no
        else:
            self.tail.proximo = novo_no
            novo_no.anterior   = self.tail
        self.tail = novo_no
    
    # INSERE NO FIM DA LISTA
    def inserePos_X(self, s, v1, v2, p):
        
        # se lista estiver vazia
        if self.head is None:
            self.inserePrimeiro(s,v1,v2,p)
        else:
            atual = self.head
            while atual.valor1 < v1:
                atual = atual.proximo
                if atual is None: break
            
            if atual == self.head:
                self.inserePrimeiro(s,v1,v2,p)
            else:
                if atual is None:
                    self.insereUltimo(s,v1,v2,p)
                else:
                    novo_no = No(p,s,v1,v2,None,None)
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
        
    def exibeLista(self):
        
        aux = self.head
        str = []
        while aux != None:
            linha = []
            linha.append(aux.estado)
            linha.append(aux.valor1)            
            str.append(linha)
            aux = aux.proximo
        
        return str
    
    def exibeArvore(self):
        
        atual = self.tail
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    def exibeArvore1(self,s):

        
        atual = self.head
        while atual.estado != s:
            atual = atual.proximo
    
        caminho = []
        atual = atual.pai
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def exibeArvore2(self, s, v1):
        
        atual = self.tail
        
        while atual.estado != s or atual.valor1 != v1:
            atual = atual.anterior
        
        caminho = []
        while atual.pai is not None:
            caminho.append(atual.estado)
            atual = atual.pai
        caminho.append(atual.estado)
        return caminho
    
    
    def primeiro(self):
        return self.head
    
    def ultimo(self):
        return self.tail

class busca(object):
    
    def custo_uniforme(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")

                return caminho, atual.valor2
        
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 # f1(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      
    
    def heuristica(self, no, custo, destino):
            
            h = []
            for i in range(len(nos)):
                if no == destino:
                    h.append(0)
                else:
                    valor = custo*random.uniform(0.1, 0.9)
                    h.append(valor)
                    
            return h

    def greedy(self, inicio, fim):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")

                return caminho, atual.valor2
        
            
            h = self.heuristica(atual.estado, atual.valor2, fim)
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = h[ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"      

    def a_estrela(self, inicio, fim,):
        
        l1 = lista()
        l2 = lista()
        visitado = []
        
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
        
        while l1.vazio() == False:
            atual = l1.deletaPrimeiro()
            
            if atual.estado == fim:
                caminho = []
                caminho = l2.exibeArvore2(atual.estado,atual.valor1)
                #print("Cópia da árvore:\n",l2.exibeLista())
                #print("\nÁrvore de busca:\n",l1.exibeLista(),"\n")

                return caminho, atual.valor2
        
            h = self.heuristica(atual.estado, atual.valor2, fim)
            ind = nos.index(atual.estado)
            for novo in grafo[ind]:
                
                ind1 = nos.index(novo[0])
                
                # CÁLCULO DO CUSTO DA ORIGEM ATÉ O NÓ ATUAL
                v2 = atual.valor2 + novo[1]  # custo do caminho
                v1 = v2 + h[ind1] # f2(n)

                flag1 = True
                flag2 = True
                for j in range(len(visitado)):
                    if visitado[j][0]==novo[0]:
                        if visitado[j][1]<=v2:
                            flag1 = False
                        else:
                            visitado[j][1]=v2
                            flag2 = False
                        break

                if flag1:
                    l1.inserePos_X(novo[0], v1 , v2, atual)
                    l2.inserePos_X(novo[0], v1, v2, atual)
                    if flag2:
                        linha = []
                        linha.append(novo[0])
                        linha.append(v2)
                        visitado.append(linha)
                    
        return "Caminho não encontrado"

nos = ["ARGENTINA", "BOLIVIA", "BRASIL", "CANADA", "CHILE", "COLOMBIA", "COSTA RICA", "CUBA", "REPUPLICA DOMINICANA", "EQUADOR",
"GUIANA FRANCESA", "GROELANDIA", "GUATEMALA", "JAMAICA", "MEXICO", "NICARAGUA", "PERU", "PARAGUAI", "ESTADOS UNIDOS", "URUGUAI", "VENEZUELA"]

grafo = [
        #argentina
        [["BRASIL", 2922], ["CHILE", 1238], ["PARAGUAI", 1735], ["URUGUAI", 1255]],
        #bolivia
        [["COLOMBIA", 5361], ["PERU", 1468], ["PARAGUAI", 1334]],
        #brasil
        [["ARGENTINA", 2922], ["COLOMBIA", 7228], ["ESTADOS UNIDOS", 8471], ["NICARAGUA", 5826], ["VENEZUELA", 3973]],
        #canada
        [["ESTADOS UNIDOS", 2260], ["GROELANDIA", 3337], ["MEXICO", 3624], ["NICARAGUA", 4410]],
        #chile
        [["ARGENTINA", 1238], ["COLOMBIA", 6434], ["PARAGUAI", 2147], ["URUGUAI", 1914]],
        #colombia
        [["BOLIVIA", 5361], ["BRASIL", 7228], ["CHILE", 6434], ["COSTA RICA", 1191], ["EQUADOR", 1493],  ["NICARAGUA", 1511]],
        #costa rica
        [["COLOMBIA", 1191], ["GUATEMALA", 1445], ["MEXICO", 3392]],
        #cuba
        [["GUATEMALA", 1457], ["JAMAICA", 383], ["NICARAGUA", 1243]],
        #republica dominicana
        [["ESTADOS UNIDOS", 3214], ["GUIANA FRANCESA", 2476], ["JAMAICA", 2479], ["VENEZUELA", 4122]],
        #equador
        [["COLOMBIA", 1493], ["PERU", 890]],
        #guiana francesa
        [["REPUPLICA DOMINICANA", 2476], ["VENEZUELA", 1515]],
        #groelandia
        [["CANADA", 3337], ["ESTADO UNIDOS", 5684]],
        #guatemala
        [["COSTA RICA", 1445], ["CUBA", 1457], ["ESTADOS UNIDOS", 5684]],
        #jamaica
        [["CUBA", 1457], ["COSTA RICA", 1445], ["MEXICO", 2004], ["NICARAGUA", 1057]],
        #mexico
        [["CANADA", 3624], ["ESTADOS UNIDOS", 1922], ["GUATEMALA", 2004]],
        #nicaragua
        [["BRASIL", 5826], ["CANADA", 4410], ["COLOMBIA", 1511], ["CUBA", 1243], ["ESTADOS UNIDOS", 4309], ["GUATEMALA", 1057], ["VENEZUELA", 2160]],
        #peru
        [["BOLIVIA", 1468], ["EQUADOR", 890]],
        #paraguai
        [["ARGENTINA", 1735], ["BOLIVIA", 1334], ["CHILE", 2147]],
        #estados unidos
        [["BRASIL", 8471], ["CANADA", 2260], ["GROELANDIA", 5684], ["MEXICO", 1922], ["NICARAGUA", 4309]],
        #uruguai
        [["ARGENTINA", 1255], ["CHILE", 1914]],
        #venezuela
        [["BRASIL", 3973], ["REPUPLICA DOMINICANA", 4122], ["GUIANA FRANCESA", 1515], ["JAMAICA", 1741], ["NICARAGUA", 2160]]
        ]
     

hea = busca()
caminho = []