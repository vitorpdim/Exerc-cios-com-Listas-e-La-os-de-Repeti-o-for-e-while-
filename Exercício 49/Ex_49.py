'''
Crie um dicionário aninhado, onde a chave é o nome de um país e o valor é
outro dicionário com as chaves: capital e população. Use laços for aninhados
para imprimir a capital de todos os países.
'''
paises = {
    "Brasil": {"capital": "Brasília", "populacao": 213000000},
    "Argentina": {"capital": "Buenos Aires", "populacao": 45000000},
    "França": {"capital": "Paris", "populacao": 67000000},
    "Japão": {"capital": "Tóquio", "populacao": 126000000},
    "Canadá": {"capital": "Ottawa", "populacao": 38000000}
}

for pais, info in paises.items():
    capital = info["capital"]
    populacao = info["populacao"]
    print(f"A capital de {pais} é {capital}. População: {populacao}")

