numeros = [10, 25, 40, 55, 30, 70, 45, 90]
i = 0
while i < len(numeros):
    numero_atual = numeros[i]
    if numero_atual > 50:
        print(f"Encontrado um número maior que 50: {numero_atual}. Parando o laço.")
        break
    print(numero_atual)
    i += 1