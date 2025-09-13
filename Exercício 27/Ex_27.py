'''
Crie uma lista de 10 números. Use um laço for para encontrar a mediana da
lista (após ordená-la).
'''
import random
numeros = random.sample(range(0,50),10)

# Ordenar a lista
numeros.sort()

# Como temos 10 números (par), a mediana é a média dos dois do meio
# índices do meio: 4 e 5 (0-based)
mediana = (numeros[4] + numeros[5]) / 2

print("Lista ordenada:", numeros)
print("Mediana:", mediana)