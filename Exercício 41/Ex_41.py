'''
Crie um dicionário com 5 nomes de pessoas e suas idades. Use um laço for para
criar uma nova lista contendo apenas os nomes das pessoas com mais de 30
anos.
'''
import random

nomes = ["Carlos", "Ana", "Fernanda", "João", "Beatriz"]

pessoas = {nome: random.randint(18, 60) for nome in nomes}

nomes_maiores_30 = []

for nome, idade in pessoas.items():
    if idade > 30:
        nomes_maiores_30.append(nome)

print("Idades geradas:", pessoas)
print("Pessoas com mais de 30 anos:", nomes_maiores_30)