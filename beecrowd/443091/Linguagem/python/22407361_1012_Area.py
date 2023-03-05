initialString = input().split(' ')  
A = float(initialString[0])
B = float(initialString[1])
C = float(initialString[2])

pi = 3.14159
areaTriangulo = A * C / 2.0
areaCirculo = C * C * pi
areaTrapezio = ( (A + B) * C) / 2.0
areaQuadrado = B * B
areaRetangulo = A * B

print("TRIANGULO:", f'{areaTriangulo:.3f}')
print("CIRCULO:", f'{areaCirculo:.3f}')
print("TRAPEZIO:", f'{areaTrapezio:.3f}')
print("QUADRADO:", f'{areaQuadrado:.3f}')
print("RETANGULO:", f'{areaRetangulo:.3f}')