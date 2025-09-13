cidades = {
    "São Paulo": 12396372,
    "Rio de Janeiro": 6775561,
    "Brasília": 3094325,
    "Salvador": 2900319,
    "Curitiba": 1963726,
    "Campinas": 950000
}
print("Cidades com mais de 1 milhão de habitantes:")
for cidade, populacao in cidades.items():
    if populacao > 1000000:
        print(f"- {cidade} (População: {populacao})")