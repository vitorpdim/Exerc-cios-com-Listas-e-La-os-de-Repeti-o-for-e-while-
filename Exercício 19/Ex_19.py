'''
Crie uma lista de 10 números. Use um laço for para calcular a média dos
números pares.
'''
import random

numeros = random.sample(range(0, 101),10)

soma_pares = 0
contagem_pares = 0

print("Os números sorteados foram:", numeros)
# Laço for para verificar cada número
for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
        contagem_pares += 1

# Calcular a média (verificando se há pares)
if contagem_pares > 0:
    media_pares = soma_pares / contagem_pares
    print("A média dos números pares é:", media_pares)
else:
    print("Não há números pares na lista.")