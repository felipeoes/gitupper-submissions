entrada = input().split(" ")N = int(entrada[0])  # tamanho vetor
I = int(entrada[1])  # valor máximo soma
F = int(entrada[2])  # valor mínimo da soma
vetor = input().split(" ")
vetor = list(map(int, vetor))
numerosFormados = []

if(N <= 1000 and N >= 2 and (I and F) <= 2000 and (I and F) >= -2000):
    pares = 0

    for i in range(len(vetor) - 1):
        for j in range(len(vetor[i:-1]) - 1):
            resultado = vetor[i] + vetor[j]
            if(resultado >= I and resultado <= F):
                # numerosFormados.append(str(vetor[i]) + str(vetor[j + 1]))
                print(f"{vetor[i]} + {vetor[j]} = {resultado}")
                pares += 1

    # for i in range(len(numerosFormados) - 1):
    #     elemento1 = numerosFormados[i]
    #     for j in range(len(numerosFormados) - 1):
    #         elemento2 = numerosFormados[j]
    #         if(len(elemento2) >= 4):
    #             elementoTrocado = elemento2.replace(elemento2[0], elemento2[2])
    #             elementoTrocado = elemento2.replace(elemento2[1], elemento2[3])
    #             elementoTrocado = elemento2.replace(elemento2[0], elemento2[2])
    #             print(elementoTrocado)
            # if(elemento1 == elementoTrocado):
            #     numerosFormados.remove(elemento2)
            #     pares -= 1

# numerosFormados = list( dict.fromkeys(numerosFormados) )
# paresNumeros = len(numerosFormados)
# print(invertido)
print(pares)
