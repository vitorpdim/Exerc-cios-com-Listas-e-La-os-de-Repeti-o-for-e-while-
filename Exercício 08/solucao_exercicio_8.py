numeros = [15, 7, 22, 48, 9, 35, 51, 12, 60, 4]
maior_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero
print(f"O maior número da lista é: {maior_numero}")