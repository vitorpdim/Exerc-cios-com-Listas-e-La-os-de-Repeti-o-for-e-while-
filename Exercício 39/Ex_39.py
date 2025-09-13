'''
Crie um dicionário com 5 nomes de países e suas capitais. Use um laço for para
encontrar e imprimir a capital do país 'Brasil'
'''
paises = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa"
}

for pais, capital in paises.items():
    if pais == "Brasil":
        print("A capital do Brasil é:", capital)
