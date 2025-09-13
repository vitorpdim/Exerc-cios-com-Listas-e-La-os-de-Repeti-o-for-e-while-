'''
Crie uma lista de 7 números. Use um laço for para imprimir apenas os números
que são múltiplos de 3.
'''

import random

numeros = random.sample(range(0, 11), 7)

print("Números gerados: ", numeros) 

for numero in numeros:
    if numero % 3 == 0:
        print(numero, "é múltiplo de três.")