produto = {
    "nome": "Notebook Gamer",
    "preco": 5500.00,
    "disponivel": False
}
for chave, valor in produto.items():
    if chave == "disponivel":
        if valor:
            print(f"O produto {produto['nome']} está disponível.")
        else:
            print(f"O produto {produto['nome']} está indisponível.")