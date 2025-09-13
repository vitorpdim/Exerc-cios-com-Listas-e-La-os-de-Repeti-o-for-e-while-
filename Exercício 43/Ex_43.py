'''
Crie um dicionário que conte a frequência de cada letra em uma frase. Exemplo:
{'a': 3, 'b': 1, ...}. Use um laço for para percorrer a frase e atualizar o dicionário
'''
frase = "May the force be with you"

frequencia = {}

for letra in frase.lower():  
    if letra.isalpha():    
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

print("Frequência das letras:", frequencia)