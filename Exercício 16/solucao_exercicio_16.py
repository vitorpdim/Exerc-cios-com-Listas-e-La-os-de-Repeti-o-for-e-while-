numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Lista original: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")