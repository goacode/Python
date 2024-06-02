print("""
============================
        Banco Bogas
============================
Valores disponiveis para Saque
R$50 - R$20 - R$10 - R$1
""")

total = saque = int(input("Quanto deseja sacar? R$"))
valor_nota = 50
total_notas = 0
while True:
    if total >= valor_nota:
        total -= valor_nota
        total_notas += 1
    else:
        if total_notas > 0:
            print(f"Total de {total_notas} cédulas de R${valor_nota}")

        if valor_nota == 50:
            valor_nota = 20

        elif valor_nota == 20:
            valor_nota = 10

        elif valor_nota == 10:
            valor_nota = 1

        total_notas = 0

        if total == 0:
            break

print("============================")
print("Volte sempre!")

        