'''
Crie um dicionário que armazene o estoque de uma loja, com o nome do
produto como chave e a quantidade como valor. Use um laço for para imprimir
a mensagem 'Estoque baixo!' para todos os produtos com menos de 10
unidades.
'''
import random

produtos = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Óleo", "Leite", "Pão", "Café", "Sal", "Manteiga"]

estoque = {produto: random.randint(0, 30) for produto in produtos}

print("Estoque gerado:", estoque)

for produto, quantidade in estoque.items():
    if quantidade < 10:
        print(f"Estoque baixo! Produto: {produto}, Quantidade: {quantidade}")