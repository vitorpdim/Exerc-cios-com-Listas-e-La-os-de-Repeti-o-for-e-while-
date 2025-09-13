produtos = {
    "arroz": 25.50,
    "feijão": 8.90,
    "óleo": 9.00,
    "sal": 2.20,
    "açúcar": 5.75
}
valor_total = 0
for preco in produtos.values():
    valor_total += preco
print(f"O valor total da compra é: R$ {valor_total:.2f}")