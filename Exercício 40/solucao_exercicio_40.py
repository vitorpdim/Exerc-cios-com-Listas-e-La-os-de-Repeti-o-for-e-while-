frutas_cores = {
    "maçã": "vermelha",
    "banana": "amarela",
    "uva": "roxa",
    "laranja": "laranja"
}
print(f"Dicionário antes da adição: {frutas_cores}")
frutas_cores["morango"] = "vermelho"
print("\nDicionário após adicionar 'morango':")
for fruta, cor in frutas_cores.items():
    print(f"- {fruta}: {cor}")