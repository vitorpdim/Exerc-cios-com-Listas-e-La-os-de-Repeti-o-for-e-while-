livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"titulo": "Iracema", "autor": "José de Alencar"}
]
autor_procurado = "Machado de Assis"
print(f"Livros de {autor_procurado}:")
for livro in livros:
    if livro["autor"] == autor_procurado:
        print(f"- {livro['titulo']}")