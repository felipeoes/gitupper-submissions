entrada1 = input().split(" ")N = int(entrada1[0])
M = int(entrada1[1])

velocidades = input().split(" ")
qtdeItens = input().split(" ")

atendentesLivres = []
tempoTotal = []

def atenderCliente(indice, qtdItens, velocidade):
    global tempoTotal
    
    tempoTotal.append(velocidade * qtdItens)
    atendentesLivres.append(indice)

def escolheMelhorFuncionario(N: int, indiceCliente):
    proximoFuncionario = 0
    
    for i in range(N - 1):
        if (velocidades[i] * qtdeItens[indiceCliente]) >= (velocidades[i+1] * qtdeItens[indiceCliente]):
            proximoFuncionario = i
    return proximoFuncionario
        

for i in range(M):
    if(i > N):
        i = escolheMelhorFuncionario(N, i)
    if(len(velocidades) > i):
        atenderCliente(i, int(qtdeItens[i]), int(velocidades[i]))
    else:
        tempoTotal.append(int(velocidades[0]) * int(qtdeItens[i]))

print(sum(set(tempoTotal)))