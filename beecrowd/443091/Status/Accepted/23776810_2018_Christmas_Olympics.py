import sys
grafo = {}


def calcula_placar(linhas: list, i: int):
    if linhas[i] not in grafo:
        grafo[linhas[i]] = [1, 0, 0]

    else:
        lista = grafo.get(linhas[i])
        lista[0] += 1
        grafo.update({linhas[i]: lista})

    if linhas[i+1] not in grafo:
        grafo[linhas[i+1]] = [0, 1, 0]

    else:
        lista = grafo.get(linhas[i+1])
        lista[1] += 1
        grafo.update({linhas[i+1]: lista})

    if linhas[i+2] not in grafo:
        grafo[linhas[i+2]] = [0, 0, 1]

    else:
        lista = grafo.get(linhas[i+2])
        lista[2] += 1
        grafo.update({linhas[i+2]: lista})


linhas = sys.stdin.read().strip().split('\n')

for i in range(1, len(linhas), 4):
    calcula_placar(linhas, i)

grafo = dict(
    sorted(grafo.items(), key=lambda item: item[0]))
grafoOrdenado = dict(
    sorted(grafo.items(), key=lambda item: item[1], reverse=True))

print("Quadro de Medalhas")
for pais in grafoOrdenado:
    print(
        pais + f" {grafoOrdenado.get(pais)[0]} {grafoOrdenado.get(pais)[1]} {grafoOrdenado.get(pais)[2]}")
