'''
Crie um dicionário com 3 nomes de cidades e seus respectivos estados. Use um
laço for para imprimir cada par de chave e valor.
'''
cidades_estados = {
    "São Paulo": "SP",
    "Rio de Janeiro": "RJ",
    "Belo Horizonte": "MG"
}

for cidade, estado in cidades_estados.items():
    print(f"Cidade: {cidade}, Estado: {estado}")