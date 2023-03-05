import sys
resp = []
resposta = []
visitados = set()

def erase(string, pos):
    splited = [char for char in string]
    splited.remove(splited[pos])
    resp = ''
    for c in splited:
        resp += c
    return resp
            

def verificaLinhas(line: str):
    visitTemp = list(visitados)
    # if line in visitTemp:
    #     if visitTemp.index(line) != len(visitTemp):
    #         return
    if line in visitados  and line != visitTemp[len(visitados) - 1]:
        return
    
    #if (memo.find(argumento) != memo.end()) return;

    if (len(line) == 1):
        visitados.add(line)
        return
    
    visitados.add(line)
    
    for i in range(len(line)):
        aux = line
        posicao = aux.index(aux[0]) + i
        aux = erase(aux, posicao)
        verificaLinhas(aux)    
        
    return 


linhas = sys.stdin.read().strip().split('\n')

for l in linhas:
    verificaLinhas(l)

    for visitado in sorted(visitados):
        print(visitado)
        
    visitados.clear()
    resposta.clear()
    print()