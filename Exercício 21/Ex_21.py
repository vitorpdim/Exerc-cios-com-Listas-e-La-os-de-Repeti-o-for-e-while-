'''
Crie uma lista de 5 nomes de pessoas. Use um laço for para criar uma nova lista
que contenha apenas os nomes com mais de 5 letras.
'''
nomes = ["Carlos", "Ana", "Fernanda", "João", "Beatriz", "Vinicius", "Giovanna", "Bruno", "Joana"]

nomes_grandes = []

for nome in nomes:
    if len(nome) > 5:
        nomes_grandes.append(nome)

print("Lista original:", nomes)
print("Nomes com mais de 5 letras:", nomes_grandes)