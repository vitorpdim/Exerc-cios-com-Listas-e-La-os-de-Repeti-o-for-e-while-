funcionarios = {
    "Ana": 3000.00,
    "Beto": 4500.00,
    "Carlos": 6000.00,
    "Diana": 2500.00
}
aumento_percentual = 0.10
print("Salários atualizados com 10% de aumento:")
for funcionario, salario in funcionarios.items():
    novo_salario = salario * (1 + aumento_percentual)
    funcionarios[funcionario] = novo_salario
    print(f"- {funcionario}: R$ {novo_salario:.2f}")
print(f"\nDicionário final: {funcionarios}")