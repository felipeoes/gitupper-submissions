# FELIPE OLIVEIRA DO ESPIRITO SANTO - NUSP: 11925242
import sys

grafo = {} # variável para guardar os paises e suas respectivas medalhas


def calcula_placar(linhas: list, i: int): # funcao que recebe as linhas de entrada como parametro e o indice i e popula o grafo conforme os paises vao surgindo nas linhas
    if linhas[i] not in grafo: # se o pais ainda não está no grafo, inicializa ele com sua respectiva medalha obtida na modalidade i-1
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


linhas = sys.stdin.read().strip().split('\n') # leitura eof do programa

for i in range(1, len(linhas), 4):
    calcula_placar(linhas, i)

grafo = dict( # ordena o grafo em ordem alfabetica para fins de desempate
    sorted(grafo.items(), key=lambda item: item[0]))
grafoOrdenado = dict( # ordena o grafo em ordem de melhor lista de medalhas, sendo ouro seguido de prata e por fim bronze
    sorted(grafo.items(), key=lambda item: item[1], reverse=True))

print("Quadro de Medalhas")
for pais in grafoOrdenado:
    print(
        pais + f" {grafoOrdenado.get(pais)[0]} {grafoOrdenado.get(pais)[1]} {grafoOrdenado.get(pais)[2]}") # printa a saída final
