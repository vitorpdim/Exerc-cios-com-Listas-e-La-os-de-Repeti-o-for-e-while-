'''
Crie um dicionário com chaves sendo números e valores sendo seus quadrados.
Use um laço for para preencher este dicionário de 1 a 10.
'''
import random

numeros = random.sample(range(1, 21), 10)

quadrados = {}

for numero in numeros:
    quadrados[numero] = numero ** 2

print("Números gerados:", numeros)
print("Dicionário de números e seus quadrados:", quadrados)