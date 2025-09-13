'''
Crie uma lista com 10 nomes de pessoas. Use um laço while para imprimir os
nomes um por um, parando quando encontrar o nome "Ana".
'''
import random

nomes = ["Carlos", "João", "Mariana", "Ana", "Lucas", "Fernanda", "Paulo", "Beatriz", "Rafael", "Carla"]

random.shuffle(nomes)

i = 0

while i < len(nomes):
    print(nomes[i])
    if nomes[i] == "Ana":
        break
    i += 1