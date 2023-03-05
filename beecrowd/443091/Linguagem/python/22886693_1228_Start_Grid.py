##Para cada caso de teste imprima uma linha contendo um único número inteiro, que indica o número mínimo de ultrapassagens necessárias para se chegar do grid de largada ao grid de chegada.
import sys

linhas = sys.stdin.read().strip().split('\n')

def calculaMinimoUltrapassagens(ordemLargada: list, ordemChegada: list):
    numeroUltrapassagens = 0
    for elemento in ordemChegada:
        posicaoLargada = ordemLargada.index(elemento)
        posicaoChegada = ordemChegada.index(elemento)
        if(posicaoChegada < posicaoLargada):
            ultrapassagens = posicaoLargada - posicaoChegada
            numeroUltrapassagens += ultrapassagens
    return numeroUltrapassagens
                
            
    
for i in range(0, len(linhas) - 1, 3):
    qtdeCompetidores = linhas[i]
    ordemLargada = linhas[i+1].split(" ")
    ordemChegada = linhas[i+2].split(" ")
    resultado = calculaMinimoUltrapassagens(ordemLargada, ordemChegada)
    print(resultado)
    