import sysimport math

entrada = sys.stdin.read().strip().split('\n')
N = int(entrada[0].split(" ")[0])
L = int(entrada[0].split(" ")[1])

ciclos = [int(elemento) for elemento in entrada[1].split(" ")]
listaPeriodos = []
ciclo = {}


def calculateT(L: int, novoLimite: int):
    for i in range(2, L, 1):  
        mmc = math.lcm(novoLimite, i)
        
        if mmc == L:
            ciclo.update({mmc:1})
            return
            
        if not ciclo:
            ciclo.update({mmc: i})
        if mmc < L and mmc > list(ciclo)[-1]:
            ciclo.update({mmc: i})


novoLimite = 1
for i in range(len(ciclos)):
    novoLimite = math.lcm(ciclos[i], novoLimite)

calculateT(L, novoLimite)
print(ciclo[max(ciclo)])
