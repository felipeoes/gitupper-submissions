# Temos um vetor de N inteiros distintos e dois inteiros I e F. Precisamos computar quantos pares desses inteiros do vetor somam pelo menos I e no máximo F. Por exemplo, se o vetor for [45, 12, 11, 7, 83, 29, 5] e I = 19 e F = 52, temos exatamente 8 pares cuja soma está entre 19 e 52: {5, 29}, {5, 45}, {7, 12}, {7, 29}, {7, 45}, {11, 12}, {11, 29} e {12, 29}.entrada = input().split(" ")
N = int(entrada[0])  # tamanho vetor
I = int(entrada[1])  # valor máximo soma
F = int(entrada[2])  # valor mínimo da soma
vetor = input().split(" ")
vetor = list(map(int, vetor))
numerosFormados = []

if(N <= 1000 and N >= 2 and (I and F) <= 2000 and (I and F) >= -2000):
    pares = 0

    for i in range(len(vetor)):
        j = i
        while(j < len(vetor) - 1):
            # for j = index in range(len(vetor)):
            resultado = vetor[i] + vetor[j + 1]
            if(resultado >= I and resultado <= F):
                # numerosFormados.append(str(vetor[i]) + str(vetor[j + 1]))
                # print(f"{vetor[i]} + {vetor[j + 1]} = {resultado}")
                pares += 1
            j += 1
# print(invertido)
print(pares)
# print(numerosFormados)
