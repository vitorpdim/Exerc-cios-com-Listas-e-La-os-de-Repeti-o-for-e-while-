'''
Crie uma lista de 5 palavras. Use um laço for para criar uma nova lista que
contenha as palavras ao contrário
'''
palavras = ["python", "cachorro", "computador", "amigo", "escola"]

palavras_invertidas = []

for palavra in palavras:
    palavras_invertidas.append(palavra[::-1])

print("Lista original:", palavras)
print("Lista invertida:", palavras_invertidas)