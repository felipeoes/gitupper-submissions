import sys

maisVeloz = 0

linhas = sys.stdin.read().strip().split('\n')

def verificaVelocidade(qtdeLesmas: int, velocidades: list):
    velocidadesConvertida = [ int(elemento) for elemento in velocidades]
    maisVeloz = max(velocidadesConvertida)
    if(maisVeloz  < 10):
        return 1
    elif(maisVeloz >= 10 and maisVeloz < 20):
        return 2
    else:
        return 3
    
    
for l in range(0, len(linhas), 2):
    print(verificaVelocidade(int(linhas[l]), linhas[l+1].split(" ")))
