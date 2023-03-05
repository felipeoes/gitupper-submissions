entrada = input().split(" ")N = int(entrada[0])  # tamanho vetor
I = int(entrada[1])  # valor máximo soma
F = int(entrada[2])  # valor mínimo da soma
# N = 2
# I = -2
# F = 2
vetor = input().split(" ")
vetor = list(map(int, vetor))
# vetor = [12, 16]
numerosFormados = []

if(N <= 1000 and N >= 2 and (I and F) <= 2000 and (I and F) >= -2000):
    pares = 0

    for i in range(len(vetor) - 2):
        for j in range(len(vetor) - 1):
            resultado = vetor[i] + vetor[j + 1]
            if(resultado > I and resultado < F):
                numerosFormados.append(vetor[i])
                numerosFormados.append(vetor[j + 1])

                pares += 1


    print(pares)