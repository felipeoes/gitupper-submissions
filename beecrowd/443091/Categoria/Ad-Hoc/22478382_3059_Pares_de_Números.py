entrada = input().split(" ")N = int(entrada[0])  # tamanho vetor
I = int(entrada[1])  # valor máximo soma
F = int(entrada[2])  # valor mínimo da soma
vetor = input().split(" ")
vetor = list(map(int, vetor))
numerosFormados = []

if(N <= 1000 and N >= 2 and (I and F) <= 2000 and (I and F) >= -2000):
    pares = 0

    for i in range(len(vetor)):
        for j in range(len(vetor) - 1):
            resultado = vetor[i] + vetor[j + 1]
            if(resultado >= I and resultado <= F):
                numerosFormados.append(vetor[i])
                numerosFormados.append(vetor[j + 1])

                pares += 1


    print((pares + 1) // 2)
