numeros_originais = [1, 2, 3, 4, 5, 6, 7, 8]
numeros_pares = []
for numero in numeros_originais:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f"Lista original: {numeros_originais}")
print(f"Nova lista com números pares: {numeros_pares}")