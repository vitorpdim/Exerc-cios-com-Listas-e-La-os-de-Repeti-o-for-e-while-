'''
Crie uma lista de 5 strings, onde cada string representa um número. Use um
laço for para converter cada string para um número inteiro e armazenar em
uma nova lista.
'''
import random

strings = random.sample(range(0, 11), 5)


numeros = []


for s in strings:
    numeros.append(int(s))

print("Lista original (strings):", strings)
print("Lista convertida (inteiros):", numeros)