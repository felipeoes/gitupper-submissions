import syssys.setrecursionlimit(1000)

def makeList(graph: dict, K: int):
    list = []
    for x in graph:
        if len(graph[x])>=K:
            list.append(x)
    return list

def makeS(lista: list, graph: dict):
    result = []   
    for x in lista:
        checking = True
        aux = graph[x]
        for element in aux:
            if element not in lista:
                checking = False
        if checking:
            result.append(x)
    return set(result)

def check(arr1: set, arr2: set, K):
    intersecao = arr1.intersection(arr2)
    if len(intersecao)>=K-1:
        return True
    return False

def finalCheck(graph: dict, maiorCaminho: set):
    listaFinal = maiorCaminho.copy()
    # for x in maiorCaminho:
    #     if set(x).intersection == 0:
    for i in range(len(maiorCaminho)):
        elemento1 = list(maiorCaminho)[i]
        for j in range(len(maiorCaminho)):
            if len(listaFinal) > j:
                elemento2 = list(listaFinal)[j]
                if len(set(graph[elemento1]).intersection(set(graph[elemento2]))) >= K-1:
                    continue
                else:
                    listaFinal.remove(elemento1)
                    break
    # for elemento in maiorCaminho:
    #     if len(set(graph[elemento]).intersection(maiorCaminho)) >= K-1:
    #         continue
    #     else:
    #         listaFinal.remove(elemento)
    #         # break
    #         continue
    return listaFinal
    
    
def computeE(calls: list, e):
    resp = []
    for x in calls:
        if x[0] == e:
            resp.append(x[1])
        if x[1] == e:
            resp.append(x[0])
    return resp

caminhos = []        
def graphPath (graph: dict, vertexS, vertexT):
    pathR(graph,vertexS, vertexT)
    
indicesVisitados = []
conjuntoParceiros = set()
caminhoAtual = []
tamanhos = {}
intersecao = set()
listaIntersecoes = []

# def graphPathI(graph: dict, vertexS, vertexT): #versao recursiva
#     vertexV: int # vertice atual
#     vertexW: int # proximo vertice
#     k: int # varival p controle de parada
#     caminho = [0] * vertexT # vetor que guarda caminho
#     indicesVisitados = []
    
#     visited = [-1] * vertexT
#     visited[vertexS] = 0;
#     caminho[1] = vertexS;
#     k = 1 
#     vertexV = vertexS 
#     vertexW = 1;
    
#     while( k!= 1 or vertexW != vertexT):
#         if(vertexW == vertexT):
#             vertexW = lista[vertexV+1]
#             k -= 1
#             vertexV = caminho[k - 1]
#         elif vertexW in graph[vertexV] and visited[vertexW] == -1:
#             visited[vertexW] = 0
#             k += 1
#             caminho[k] = vertexW
#             vertexV = vertexW
#             if vertexW == vertexT:
#                 break
#             vertexW = lista[0]
#         else:
#             vertexW = lista[lista.index(vertexV) + 1]
#             # vertexW += 1
#     if visited[vertexT == -1]:
#         return 0 
#     else:
#         return 1

calculoLigacoes = []
            

def pathR (graph: dict, vertexV, vertexT): #versao recursiva
    if(vertexV == vertexT):
        return
    visited[vertexV - 1] = 0; # marcando esse vértice como visitado
    
    for w in lista:
        if(w == vertexT):
            caminhoGravado = set(caminhoAtual)
            tamanhos.update({len(caminhoGravado):caminhoGravado})
            caminhos.append(caminhoGravado)
            caminhoAtual.remove(vertexV)
            break
        if(w in graph[vertexV]):
            if(visited[w - 1] == -1):
                indicesVisitados.append(w)
                caminhoAtual.append(w)
                for x in listaIntersecoes:
                    if w not in x:
                        if(vertexV in lista):
                            calculoLigacoes.append(vertexV)
                        break
                pathR(graph, w, vertexT)     
                 
    intersecao = set(graph[vertexV]).intersection(*listaIntersecoes)
    listaIntersecoes.append(intersecao)  
    

n = input().split(" ")
N = int(n[0])
P = int(n[1])
K = int(n[2])

while (True):
    graph = {}
    calls = []
       
    for x in range(P):
        aux = [int(x) for x in input().split()]
        calls.append(aux)
    if K==1 or (P == 0):
        if P == 1:
            print(N)
        else:
            print(P)

    else:
        for e in range(1,N+1):
            graph.update({e:computeE(calls, e)})

        lista = makeList(graph, K)
        # S = makeS(lista, graph)
        
        # if(len(lista) == 1):
        #     print(1 + len(graph[lista[0]]))
            
        # else:    
        vertexT = lista[len(lista) - 1]
        visited = [-1] * vertexT
        caminhoAtual.append(lista[0])
        conjuntoParceiros.update(set(graph[lista[0]]))
        graphPath(graph, lista[0], vertexT)
        
        if(tamanhos):    
            maiorCaminho = tamanhos[max(tamanhos)]
            S = finalCheck(graph, maiorCaminho)
            
            if(S != None):
                print(len(S))
            else:
                print(0)
        else:
            print(0)
            # if(tamanhos):
            #     print(max(tamanhos))
            # else:
            #     print(0)
            
    indicesVisitados = []        
    visited = []
    tamanhos = {}
    caminhos = []
    listaFinal = []
    caminhoAtual = []
    
    n = input().split(" ")
    N = int(n[0])
    P = int(n[1])
    K = int(n[2])
    
    if(N == 0 and P == 0 and K == 0):
        break