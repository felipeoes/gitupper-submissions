from itertools import combinations
def computeP(graph, P):
    products = []
    for c in graph:
        if graph[c][2] == P or graph[c][3] == P:
            #print('O cliente '+str(c)+' tem o produto '+str(P))
            products.append(c)

    return products

def computePS(graph, P):
    products = []
    for c in graph:
        if graph[c][0] == P or graph[c][1] == P:
            #print('O cliente '+str(c)+' tem o produto '+str(P))
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
        #print(aux)
        
        aux = sumArr(aux, product[x])
        #print('N '+str(x)+'Soma entre'+str(aux)+' e '+str(product[x]))
        #print('Resultado :'+str(aux))
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

#linhas = sys.stdin.read().strip().split('\n')
#for l in linhas:

n = input().split(" ")
C = int(n[0])
P = int(n[1])
result = []

while(C != 0 and (P != 0)):
    graph = {}
    product = {}
    productS = {}

    aux = []
    aux1 = []
    comb = []
    combS = []
    
    clients = [c for c in range(1, C+1)]
    
           
    # Salva os votos de cada cliente
    for client in range(1, C+1):
        votes = [ int(x) for x in input().split()]
        graph.update({client:votes})   

    clientsS = adjustClientS(graph, clients)
    clientsN = adjustClientN(graph, clients)


    for p in range(1,P+1):
        product.update({p:computeP(graph, p)})
    #print(product)

    for p in range(1,P+1):
        productS.update({p:computePS(graph, p)})
    #print(productS)

    produtos = [p for p in range(1,P+1)]

    for c in range(2,P+1):
        combi = combinations(produtos, c)

        for i in combi:
            if getRelation(i, product, clientsN):
                comb.append(i)
            
            if getRelation(i, productS, clientsS):
                combS.append(i)

   
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