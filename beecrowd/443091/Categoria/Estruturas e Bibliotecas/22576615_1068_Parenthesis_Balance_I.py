import sys
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
        for i in range(len(listaParenteses) - 1):
            if( listaParenteses[i] == ")" and listaParenteses[i + 1] == "(" ):
                return False
    return True       
        


linhas = sys.stdin.read().strip().split('\n')
for l in linhas:
    #aqui a gnt chama o método auxiliar pra verificar cada linha ok ? ok
    if(verificaParenteses(l)):
        print("correct")
    print("incorrect")