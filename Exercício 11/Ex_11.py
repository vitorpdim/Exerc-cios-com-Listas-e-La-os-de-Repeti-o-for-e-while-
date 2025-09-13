'''
Crie uma lista com 10 números inteiros. Use um laço for para somar apenas os
números negativos.
'''
import random

numeros = random.sample(range(-50, 51), 10)  # range(0, 11) inclui 0 até 10

soma_negativos = 0

for numero in numeros:
    if numero < 0:
        soma_negativos += numero

print("Os números sorteados são:", numeros)
print("A soma dos números negativos é:", soma_negativos)