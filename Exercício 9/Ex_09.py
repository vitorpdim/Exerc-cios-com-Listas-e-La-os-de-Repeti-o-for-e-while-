'''
Crie uma lista de 10 números. Use um laço for para encontrar e imprimir o
menor número da lista.
'''
import random

numeros = random.sample(range(0, 101), 10)  # range(0, 11) inclui 0 até 10

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print("Números sorteados:", numeros)
print("O menor número da lista é:", menor)