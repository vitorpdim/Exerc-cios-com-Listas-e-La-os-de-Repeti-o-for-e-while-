'''
Crie uma lista de listas (uma matriz 2x3). Use laços for aninhados para imprimir
cada elemento.
'''
import random

matriz = [[random.randint(0, 9) for _ in range(3)] for _ in range(2)]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()  