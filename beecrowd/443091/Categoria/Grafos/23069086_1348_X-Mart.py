from itertools import combinations
def computeP(graph, P):
    products = []
    for c in graph:
        if graph[c][2] == P or graph[c][3] == P:
            products.append(c)

    return products

def computePS(graph, P):
    products = []
    for c in graph:
        if graph[c][0] == P or graph[c][1] == P:
            products.append(c)                          
    return products

def sumArr(arr1, arr2):
    in_first = set(arr1)
    in_second = set(arr2)

    in_second_but_not_in_first = in_second - in_first

    result = arr1 + list(in_second_but_not_in_first)
    return sorted(result)

def comparator(arr1, arr2):
    resp = True
    for x in arr1:
        for y in arr2:
            if x==y:      
                return False
            else:
                continue       
    return resp          

def adjustClientN(graph, clients):
    result = []
    for x in graph:
        if graph[x][2] == 0 and graph[x][3] == 0:
            result.append(x)
    resp = [x for x in clients if x not in result]
    return resp

def adjustClientS(graph, clients):
    result = []
    for x in graph:
        if graph[x][0] == 0 and graph[x][1] == 0:
            result.append(x)
    resp = [x for x in clients if x not in result]
    return resp

def getRelation(arr, product, clients):
    aux = []
    for x in arr:
        aux = sumArr(aux, product[x])
    if aux == clients:
        return True
    else: 
        return False

def checking(comb, combS):
    
    for x in comb:
        for y in combS:
            resp = comparator(x,y)
            if resp:
                return 'yes'    
    return 'no'

# Recebe a primeira linha e passa as variáveis C(Clientes) e P(Produtos).
n = input().split(" ") 
C = int(n[0])
P = int(n[1])
# Lista de resultados de todos os casos de teste.
result = []

# Garante que o código só vai parar quando C e P forem iguais a 0.
# T(1)
while(C != 0 and (P != 0)): # T(N-1)
    graph = {}
    product = {}
    productS = {}

    comb = []
    combS = []
    
    # Cria uma lista com todos os clientes.
    clients = [c for c in range(1, C+1)] # T(C)    
           
    # Faz um grafo de clientes que armazena os votos de cada cliente.
    for client in range(1, C+1):  # T(C) + T(C*P - 1) + T(C) = T(C*P)
        votes = [ int(x) for x in input().split()]
        graph.update({client:votes})   

    # Cria outras duas listas de clientes não levando em consideração aqueles que não votarem em nenhum produto.
    clientsS = adjustClientS(graph, clients)
    clientsN = adjustClientN(graph, clients)

    # Faz um grafo de Produtos que aparecem nos votos contra de cada cliente.
    for p in range(1,P+1): # T(P)
        product.update({p:computeP(graph, p)})

    # Faz um grafo de Produtos que aparecem nos votos a favor de cada cliente.
    for p in range(1,P+1): # T(P)
        productS.update({p:computePS(graph, p)})

    # Faz uma lista com todos os produtos.
    produtos = [p for p in range(1,P+1)] # T(P)

    for c in range(1,P+1): # T(P)
        # Lista com todas as combinações possíveis de produtos, com c elementos.
        combi = combinations(produtos, 1)

        for i in combi:
            if getRelation(i, product, clientsN):
                # Caso a combinação de votos contra atenda a todos os cliente, adiciona na lista comb.
                comb.append(i)

            if getRelation(i, productS, clientsS):
                # Caso a combinação de votos contra atenda a todos os cliente, adiciona na lista comb.
                combS.append(i)

    # Checa se há uma combinação de produtos contra e a favor que satisfaz todos os clientes.
    result.append(checking(comb, combS))

    n  = input().split(" ")
    C = int(n[0])
    P = int(n[1])   
    
    

for s in result:
    print(s)
    


#print ('Está são as combinações de voto sim: ')
#print(combS)
#print ('Está são as combinações de voto não: ')
#print(comb)



#print(product)