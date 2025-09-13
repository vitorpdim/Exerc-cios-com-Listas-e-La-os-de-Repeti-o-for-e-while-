'''
Crie um dicionário para um carro, com as chaves: marca, modelo, ano e preço.
Use um laço for para imprimir apenas os valores.

'''
import random

marcas = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen"]
modelos = ["Corolla", "Civic", "Fiesta", "Onix", "Golf"]

carro = {
    "marca": random.choice(marcas),
    "modelo": random.choice(modelos),
    "ano": random.randint(2000, 2025),
    "preco": random.randint(20000, 150000)
}

for valor in carro.values():
    print(valor)