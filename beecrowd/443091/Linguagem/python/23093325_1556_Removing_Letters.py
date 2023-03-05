import sys
sys.setrecursionlimit(1000)

def verificaLinhas(grafo: list, linha: str):
    if linha == "" or (grafo and linha in grafo and linha != grafo[-1]):
        return
    
    grafo.append(linha)
    
    if (len(linha) == 1):
        return
    
    for i in range(len(linha)):
        aux = linha
        aux = aux[:i] + aux[i+1:]
        verificaLinhas(grafo, aux)
    

linhas = sys.stdin.read().strip().split('\n')

for l in linhas:
    grafo = []
    
    verificaLinhas(grafo, l)

    for elemento in sorted(grafo):
        sys.stdout.write(elemento + "\n")
        
    sys.stdout.write("\n")