from random import shuffle
alunos = []

aluno = input("Digite o primeiro aluno: ")
alunos.append(aluno)

aluno = input("Digite o segundo aluno: ")
alunos.append(aluno)

aluno = input("Digite o terceiro aluno: ")
alunos.append(aluno)

aluno = input("Digite o quarto aluno: ")
alunos.append(aluno)

shuffle(alunos)


print(f"A ordem de apresentação será: {alunos}")