def closest(list, number):    aux = []
    for valor in list:
        aux.append(abs(number-valor))

    return aux.index(min(aux)) + 1
    
def pesquisaNumeroSecreto(qtdeAlunos, numeroSecreto, vetor):
    if(qtdeAlunos <= 10 and qtdeAlunos >= 4 and numeroSecreto <= 100 and numeroSecreto >= 1):
        vetor = list(map(int, vetor))
        posicaoAcerto = vetor[0]
        for i in range(len(vetor)):
            if(vetor[i] == numeroSecreto):
                posicaoAcerto = i + 1  # adiciona 1 na posicao pois posicao 0 não é válido no contexto
                return posicaoAcerto
        else:
            # indiceMaisProximo = min(range(len(vetor)), key=lambda x: abs(x-numeroSecreto))
            # indiceFinal = indiceMaisProximo - 1
            # return indiceFinal
            return closest(vetor, numeroSecreto)


qtdeCamisetas = int(input())
armazemRespostas = [0] * qtdeCamisetas

for i in range(qtdeCamisetas):
    linha2 = input().split(" ")
    alunos = int(linha2[0])
    numSecreto = int(linha2[1])
    vetorRespostas = input().split(" ")
    armazemRespostas[i] = pesquisaNumeroSecreto(alunos, numSecreto, vetorRespostas)

for i in range(len(armazemRespostas)):
    print(armazemRespostas[i])
