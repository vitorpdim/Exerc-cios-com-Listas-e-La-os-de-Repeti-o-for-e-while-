'''
Crie um dicionário com 5 nomes de pessoas e suas idades. Use um laço for para
imprimir o nome e a idade de cada pessoa.
'''
import random

nomes = ["Carlos", "Ana", "Fernanda", "João", "Beatriz", "Lucas", "Mariana", "Paulo", "Carla", "Rafael"]

nomes_aleatorios = random.sample(nomes, 5)

pessoas = {nome: random.randint(18, 60) for nome in nomes_aleatorios}

for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")