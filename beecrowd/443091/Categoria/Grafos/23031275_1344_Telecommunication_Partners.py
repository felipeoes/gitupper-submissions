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

def computeE(calls: list, e):
    resp = []
    for x in calls:
        if x[0] == e:
            resp.append(x[1])
        if x[1] == e:
            resp.append(x[0])
    return resp

visited = []
caminhos = []        
def graphPath (graph: dict, vertexS, vertexT):
    for v in range(vertexT):
        # visited[v] = -1
        visited.append(-1)
    pathR(graph,vertexS, vertexT)
    # if visited[len(lista) - 1] == -1:
    #     return 0 # nao existe caminho
    # else:
    #     caminhos.append(visited)
    #     return 1 # existe caminho
    
indicesVisitados = []
conjuntoParceiros = set()
caminhoAtual = []
tamanhos = []
def pathR (graph: dict, vertexV, vertexT):
    if(vertexV == vertexT):
        return
    visited[vertexV - 1] = 0; # marcando esse vértice como visitado
    conjuntoParceiros.update(set(graph[vertexV]))
    for w in lista:
        if(w in graph[vertexV] and w in conjuntoParceiros):
            if(visited[w - 1] == -1):
                indicesVisitados.append(w)
                # if(w not in )
                caminhoAtual.append(w)
                pathR(graph, w, vertexT)         
    caminhoGravado = set(caminhoAtual)            
    tamanhos.append(len(caminhoGravado) - 1)   
    caminhos.append(caminhoGravado)
    caminhoAtual.remove(vertexV)
    setRemover = set(graph[vertexV])
    # conjuntoParceiros.remove(vertexV)
    # visited[vertexV - 1] = -1
    # if(len(set(indicesVisitados)) == len(lista)):
    #     return
    
                
                

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
        # print(graph)

        lista = makeList(graph, K)
        # setElements = set()
        # setTemp = set()
        # for elemento in lista:
        #     for parceiro in graph[elemento]:
        #         setTemp = setTemp.union(set(graph[elemento]).intersection(set(graph[parceiro])))

        #         setElements = setElements.union(setTemp)
        # intersecao = [elemento for elemento, index in lista if graph[elemento][index] in lista]
        
        if(len(lista) == 1):
            print(1 + len(graph[lista[0]]))
            
        else:    
            indicesVisitados.append(lista[0])
            caminhoAtual.append(lista[0])
            resultado = graphPath(graph, lista[0], lista[len(lista) - 1])
            
            if(tamanhos):
                print(max(tamanhos))
            else:
                print(0)
        # else: 
        #     print(0)
            
    indicesVisitados = []        
    visited = []
    tamanhos = []
    caminhos = []
    n = input().split(" ")
    N = int(n[0])
    P = int(n[1])
    K = int(n[2])
    
    if(N == 0 and P == 0 and K == 0):
        break