salario = float(input("Qual é o salario do funcionario? R$"))
salario_final = salario * 1.15 if salario < 1250 else salario * 1.10
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salario_final:.2f} apos o aumento.")