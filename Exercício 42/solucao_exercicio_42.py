alunos_notas = {
    'João': [8.5, 9.0],
    'Maria': [7.0, 6.5],
    'Pedro': [10.0, 8.0, 9.5]
}
for aluno, notas in alunos_notas.items():
    media = sum(notas) / len(notas)
    print(f"A média de {aluno} é: {media:.2f}")