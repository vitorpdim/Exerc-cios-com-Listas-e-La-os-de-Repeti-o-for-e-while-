palavras = ["casa", "sol", "lua", "abacaxi", "estrela", "ovo"]
palavras_sem_a = []
for palavra in palavras:
    if 'a' not in palavra.lower():
        palavras_sem_a.append(palavra)
print(f"Lista original: {palavras}")
print(f"Lista sem palavras com a letra 'a': {palavras_sem_a}")