entrada = input().split(" ")N = int(entrada[0])  # tamanho vetor
I = int(entrada[1])  # valor máximo soma
F = int(entrada[2])  # valor mínimo da soma

if(N <= 1000 and N >= 2 and (I and F) <= 2000 and (I and F) >= -2000):
    vetor = input().split(" ")
    vetor = list(map(int, vetor))
    pares = 0

    for i in range(len(vetor) - 2):
        for j in range(len(vetor) - 2):
            result = vetor[j] + vetor[i + 1]
            if(result > I and result <= F):
                pares += 1

    print(pares)