import sysimport math

entrada = sys.stdin.read().strip().split('\n')

def calculaPrimo(num: str):
    num = int(num)
    if num == 0 or num == 1:
        return False
    for i in range(2,int(math.sqrt(num))):  
       if (num % i) == 0: 
           return False
    return True

def calculaPrimoAux(num: str):
    if len(num) >= 2:
        for algarismo in num:
            if algarismo == '0' or algarismo == '1' or algarismo == '4' or algarismo == '6' or algarismo == '8' or algarismo == '9':
                return False
    return True       

for linha in entrada:
    if calculaPrimo(linha):
        if calculaPrimoAux(linha):
            print("Super")
            continue
        print("Primo")
        continue
    print("Nada")