from random import choice
alunos = []

aluno = input("Digite o primeiro aluno: ")
alunos.append(aluno)

aluno = input("Digite o segundo aluno: ")
alunos.append(aluno)

aluno = input("Digite o terceiro aluno: ")
alunos.append(aluno)

aluno = input("Digite o quarto aluno: ")
alunos.append(aluno)

print(choice(alunos))