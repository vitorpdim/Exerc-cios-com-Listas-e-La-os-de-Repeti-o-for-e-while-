'''
Crie uma lista de 10 números. Use um laço for para imprimir a tabuada de cada
número.
'''
import random
numeros = random.sample(range(1,20),10)

print("Números escolhidos:",numeros)
for numero in numeros:
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):  # multiplicadores de 1 a 10
        print(f"{numero} x {i} = {numero * i}")
    print()