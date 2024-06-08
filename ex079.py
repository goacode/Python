valores = []

while True:
    valor = int(input("Digite um valor: "))
    if valor in valores:
        print("Valor já cadastrado.")
    else:
        valores.append(valor)
        print("Valor cadastrado com sucesso!")

    continuar = "a"
    while continuar not in "SN":
        continuar = input("Deseja continuar? [S/N]").strip().upper()[0]

    if continuar == "N":
        break

valores.sort()
print(f"Você digitou os valores: ", end="")
for valor in valores:
    print(valor, end=" ")