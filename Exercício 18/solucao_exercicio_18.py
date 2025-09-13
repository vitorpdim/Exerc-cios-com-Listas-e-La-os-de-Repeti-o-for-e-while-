numeros_com_duplicatas = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 1]
numeros_unicos = []
for numero in numeros_com_duplicatas:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)
print(f"Lista original: {numeros_com_duplicatas}")
print(f"Lista com valores únicos: {numeros_unicos}")