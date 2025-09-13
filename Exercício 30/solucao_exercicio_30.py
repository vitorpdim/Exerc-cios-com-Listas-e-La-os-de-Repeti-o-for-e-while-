palavras = ["Python", "Java", "PHP", "Perl", "C++", "Pascal"]
contador_p = 0
for palavra in palavras:
    if palavra.startswith('P'):
        contador_p += 1
print(f"Quantidade de strings que começam com 'P': {contador_p}")