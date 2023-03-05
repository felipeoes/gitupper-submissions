import sys

sys.setrecursionlimit(1000000)
    
def verificaLinhas(grafo: dict, linha: str):
    if grafo and linha in grafo and linha != grafo[linha] or linha == "":
        return
    
    grafo[linha] = linha
    
    if (len(linha) == 1):
        return
    
    for i in range(len(linha)):
        aux = linha
        aux = aux[:i] + aux[i+1:]
        verificaLinhas(grafo, aux)

linhas = sys.stdin.read().strip().split('\n')

for l in linhas:
    graph  = {}
    
    verificaLinhas(graph, l)

    for elemento in sorted(graph):
        sys.stdout.write(elemento + "\n")
        
    sys.stdout.write("\n")