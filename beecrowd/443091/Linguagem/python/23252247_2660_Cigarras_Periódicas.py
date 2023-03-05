import sys
entrada = sys.stdin.read().strip().split('\n')

def calculaPrimo(num: int):
    if num == 0 or num == 1:
        return False
    for i in range(2,num):  
       if (num % i) == 0: 
           return False
    return True

def calculaPrimoAux(num: int):
    if num > 10:
        algarismos = [int(num) for num in str(num)]
        for algarismo in algarismos:
            if not calculaPrimo(algarismo) or algarismo == 0:
                return False
    return True       

for linha in entrada:
    num = int(linha)
    if calculaPrimo(num):
        if calculaPrimoAux(num):
            print("Super")
            continue
        print("Primo")
        continue
    print("Nada")