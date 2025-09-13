hobbies_pessoas = {
    "Alice": ["leitura", "cinema", "corrida"],
    "Bruno": ["futebol", "games"],
    "Clara": ["viagem", "fotografia", "leitura"],
    "Davi": ["música", "cozinhar"]
}
hobby_procurado = "leitura"
print(f"Pessoas que gostam de '{hobby_procurado}':")
for pessoa, hobbies in hobbies_pessoas.items():
    if hobby_procurado in hobbies:
        print(f"- {pessoa}")