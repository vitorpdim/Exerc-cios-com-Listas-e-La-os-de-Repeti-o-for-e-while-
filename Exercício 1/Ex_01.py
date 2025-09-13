'''
Crie uma lista de 6 notas (valores de 0 a 10). Use um laço for para contar
quantas notas são maiores ou iguais a 7 e imprimir o total.
'''
import random

notas = random.sample(range(0, 11), 6)  # range(0, 11) inclui 0 até 10

notas_boas = []

for nota in notas:
    if nota >= 7:
        notas_boas.append(nota)

print("Notas geradas:", notas)
print("Total de notas maiores ou iguais a 7:", len(notas_boas))
print("As notas maiores ou iguais a 7 são:", notas_boas)