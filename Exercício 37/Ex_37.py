'''
Use um laço for para verificar se o valor 'Python' existe em algum valor de um
dicionário, onde as chaves são nomes de cursos e os valores são as linguagens
usadas.
'''
import random

linguagens = ["Java", "C++", "JavaScript", "Ruby", "C#", "Go"]

nomes_cursos = [f"Curso{i}" for i in range(1, 11)]

cursos = {}

tem_python = random.choice([True, False])

if tem_python:
    cursos_python = random.sample(nomes_cursos, random.randint(1, 2))
else:
    cursos_python = []

for curso in nomes_cursos:
    if curso in cursos_python:
        cursos[curso] = "Python"
    else:
        cursos[curso] = random.choice(linguagens)

encontrou = False
for curso, linguagem in cursos.items():
    if linguagem == "Python":
        print(f"Python está presente no {curso}.")
        encontrou = True

if not encontrou:
    print("Python não está presente em nenhum curso.")