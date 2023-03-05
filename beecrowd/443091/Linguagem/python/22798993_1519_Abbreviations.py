linhas = []listaAbreviacoes = []
listaSignificados = []
contagemAbreviacao = 0
entrada = ""
naoDeveAbreviar = False


# verificacao
letrasUsadas = []
palavrasAbreviadas = []

while(entrada != "."):
    entrada = input()
    linhas.append(entrada)

# True: abreviação ja foi usada
# False: abreviação não foi usada


def verificaAbrevPalavra(palavra):
    global letrasUsadas
    global contagemAbreviacao
    global listaAbreviacoes
    if len(letrasUsadas) == 0:

        letrasUsadas.append(palavra[0])
        palavrasAbreviadas.append(palavra)
        return False

    else:
        for i in range(len(letrasUsadas)):
            if (letrasUsadas[i] == palavra[0]):

                for elemento in palavrasAbreviadas:
                    if (elemento[0] == palavra[0]):

                        if(len(elemento) >= len(palavra)):
                            if(elemento == palavra):
                                return elemento
                            return True

                        else:
                            abreviacao = elemento[0] + "."
                            significado = abreviacao + " = " + elemento
                            palavrasAbreviadas.remove(elemento)
                            listaAbreviacoes = [elemento if x==abreviacao else x for x in listaAbreviacoes]
                            # listaAbreviacoes.insert(
                            #     listaAbreviacoes.index(abreviacao), elemento)
                            # listaAbreviacoes.remove(abreviacao)
                            listaSignificados.remove(significado)
                            palavrasAbreviadas.append(palavra)
                            contagemAbreviacao -= 1
                            return False

        letrasUsadas.append(palavra[0])
        palavrasAbreviadas.append(palavra)
        return False


def verificaAbrevPalavra2(palavra):
    global letrasUsadas
    global contagemAbreviacao
    global listaAbreviacoes

    if len(letrasUsadas) == 0:

        letrasUsadas.append(palavra[0])
        palavrasAbreviadas.append(palavra)
        return False

    else:
        for i in range(len(letrasUsadas)):
            if (letrasUsadas[i] == palavra[0]):

                for elemento in palavrasAbreviadas:
                    if (elemento[0] == palavra[0]):

                        if(len(elemento) >= len(palavra)):
                            if(elemento == palavra):
                                return elemento
                            abreviacao = elemento[0] + "."
                            significado = abreviacao + " = " + elemento
                            palavrasAbreviadas.remove(elemento)
                            # listaAbreviacoes = [elemento if x==abreviacao else x for x in listaAbreviacoes]
                            for i in range(len(listaAbreviacoes)):
                                if(listaAbreviacoes[i] == abreviacao):
                                    listaAbreviacoes[i] = elemento
                                    contagemAbreviacao -= 1
                                    
                            if(significado in listaSignificados):
                                listaSignificados.remove(significado)
                            palavrasAbreviadas.append(palavra)
                            # contagemAbreviacao -= 1
                            

                        else:
                            if(elemento == palavra):
                                return elemento
                            return True

        letrasUsadas.append(palavra[0])
        palavrasAbreviadas.append(palavra)
        return False


def abreviador(linha: str):
    global listaAbreviacoes
    global contagemAbreviacao
    global listaSignificados
    listaAbreviacoes = []
    contagemAbreviacao = 0
    listaSignificados = []

    palavras = linha.split(" ")
    for palavra in palavras:
        if(len(palavra) > 2):
            elemento = verificaAbrevPalavra(palavra)
            if(not(elemento)):
                letraInicial = palavra[0]
                abreviacao = letraInicial + "."
                listaAbreviacoes.append(abreviacao)
                significado = abreviacao + " = " + palavra
                listaSignificados.append(significado)
                contagemAbreviacao += 1
            else:
                if(elemento == palavra):
                    palavra = palavra[0] + "."
                listaAbreviacoes.append(palavra)
        else:
            listaAbreviacoes.append(palavra)
    return contagemAbreviacao


def abreviador2(linha: str):
    global listaAbreviacoes
    global contagemAbreviacao
    global listaSignificados
    listaAbreviacoes = []
    contagemAbreviacao = 0
    listaSignificados = []

    palavras = linha.split(" ")
    for palavra in palavras:
        if(len(palavra) > 2):
            elemento = verificaAbrevPalavra2(palavra)
            if(not(elemento)):
                letraInicial = palavra[0]
                abreviacao = letraInicial + "."
                listaAbreviacoes.append(abreviacao)
                significado = abreviacao + " = " + palavra
                listaSignificados.append(significado)
                contagemAbreviacao += 1
            else:
                if(elemento == palavra):
                    palavra = palavra[0] + "."
                listaAbreviacoes.append(palavra)
        else:

            listaAbreviacoes.append(palavra)
    return contagemAbreviacao


def imprimeSignificado(listaSignificados):
    listaSignificados.sort()
    for i in range(len(listaSignificados)):
        print(listaSignificados[i])


def comparaAbreviacoes(abreviacao0: str, abreviacao1: str):
    if(len(abreviacao0.strip()) > len(abreviacao1.strip())):
        return True
    return False


listaSignificado0 = []
listaSignificado1 = []
contagemAbreviacao0 = 0
contagemAbreviacao1 = 0
for i in range(len(linhas) - 1):
    abreviador(linhas[i])
    abreviacoes = ' '.join(listaAbreviacoes)
    listaSignificado0 = listaSignificados
    contagemAbreviacao0 = contagemAbreviacao
    letrasUsadas = []
    palavrasAbreviadas = []

    abreviador2(linhas[i])
    abreviacoes1 = ' '.join(listaAbreviacoes)
    listaSignificado1 = listaSignificados
    contagemAbreviacao1 = contagemAbreviacao

    if(comparaAbreviacoes(abreviacoes, abreviacoes1)):
        print(abreviacoes1)
        print(contagemAbreviacao1)
        imprimeSignificado(listaSignificado1)

    else:
        print(abreviacoes)
        print(contagemAbreviacao0)
        imprimeSignificado(listaSignificado0)

    letrasUsadas = []
    palavrasAbreviadas = []


# for i in range(len(linhas) - 1):
#     abreviador2(linhas[i])
#     abreviacoes = ' '.join(listaAbreviacoes)
#     print(abreviacoes)
#     print(len(abreviacoes.strip()))
#     print(contagemAbreviacao)
#     imprimeSignificado()
#     letrasUsadas = []
#     palavrasAbreviadas = []
