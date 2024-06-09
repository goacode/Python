alunos = []
aux_aluno = []
aux_notas = []
while True:
    aux_aluno.append(input("Nome: "))
    aux_notas.append(float(input("Nota 1: ")))
    aux_notas.append(float(input("Nota 2: ")))
    aux_aluno.append(aux_notas[:])
    alunos.append(aux_aluno[:])

    aux_aluno.clear()
    aux_notas.clear()

    cont = "A"
    while cont not in "SN":
        cont = input("Deseja continuar? [S/N]").strip().upper()[0]

    if cont == "N":
        break

print("=-=" * 30)
print(f"{"ID":3} {"NOME":15} {"MÉDIA":8}")
print("-" * 30)
for pos, aluno in enumerate(alunos):
    print(f"{pos:<3} {aluno[0]:15} {sum(aluno[1])/2:6.2f}")

print("-" * 30)

opcao = 0
while True:
    opcao = int(input("Digite o ID do Aluno para ver suas notas (999 para Sair) "))
    if opcao == 999:
        break
    print(f"As notas de {alunos[opcao][0]} são {alunos[opcao][1]}")
