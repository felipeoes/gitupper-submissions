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
            if algarismo == 0 or algarismo == 1 or not calculaPrimo(algarismo):
                return False
    return True       

for linha in entrada:
    num = int(linha)
    if calculaPrimo(num):
        if '0' in linha or '1' in linha:
            print("Primo")
            continue
        if calculaPrimoAux(num):
            print("Super")
            continue
        print("Primo")
        continue
    print("Nada")