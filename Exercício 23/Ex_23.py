'''
Crie duas listas de 5 números cada. Use laços for aninhados para multiplicar
cada número da primeira lista por cada número da segunda lista.
'''
import random

lista1 = random.sample(range(0,11),5)
lista2 = random.sample(range(0,11),5)

resultado = []

for num1 in lista1:
    for num2 in lista2:
        resultado.append(num1 * num2)
print("Os números são:",lista1, "e",lista2)
print("Resultado das multiplicações:", resultado)