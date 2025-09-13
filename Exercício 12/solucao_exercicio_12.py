palavras = ["Python", "Programacao", "Logica", "Computador", "Inteligencia"]
vogais = "aeiouAEIOU"
total_vogais = 0
for palavra in palavras:
    for letra in palavra:
        if letra in vogais:
            total_vogais += 1
print(f"O número total de vogais em todas as palavras é: {total_vogais}")