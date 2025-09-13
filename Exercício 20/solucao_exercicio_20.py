numeros = [1, 5, 2, 5, 3, 5, 4, 5, 5, 6]
contador_de_5 = 0
for numero in numeros:
    if numero == 5:
        contador_de_5 += 1
print(f"O número 5 aparece {contador_de_5} vezes na lista.")