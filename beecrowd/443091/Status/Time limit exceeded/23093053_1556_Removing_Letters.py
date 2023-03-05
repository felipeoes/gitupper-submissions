import sys

sys.setrecursionlimit(10000)
    
def verificaLinhas(grafo: dict, linha: str):
    if linha == "" or (grafo and linha in grafo and linha != list(grafo.keys())[-1]):
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