import sys
def checaOrdemParenteses(listaParenteses):
    continuosAbertos = 0
    continuosFechados = 0
    valorContinuosAbertos = 0
    valorContinuosFechados = 0
    for i in range(len(listaParenteses) - 1):
        if(listaParenteses[i] == "("):
            continuosFechados = 0
            continuosAbertos = continuosAbertos + 1
            valorContinuosAbertos = continuosAbertos

        else:
            continuosAbertos = 0
            continuosFechados = continuosFechados + 1
            valorContinuosFechados = continuosFechados

    if(valorContinuosAbertos != valorContinuosFechados):
        return False

    return True


def verificaParenteses(linha):
    contadorEsquerda = 0
    contadorDireita = 0
    listaParenteses = []
    for letra in linha:
        if(letra == "("):
            contadorEsquerda = contadorEsquerda + 1
            listaParenteses.append(letra)
        if(letra == ")"):
            contadorDireita = contadorDireita + 1
            listaParenteses.append(letra)
    if(contadorDireita == contadorEsquerda):
        if(not(checaOrdemParenteses(listaParenteses))):
            return False

        return True
        # if( listaParenteses[i] == ")" and listaParenteses[i + 1] == "(" ):
        #     return False


linhas = sys.stdin.read().strip().split('\n')
for l in linhas:
    # aqui a gnt chama o método auxiliar pra verificar cada linha ok ? ok
    if(verificaParenteses(l)):
        print("correct")
    print("incorrect")
