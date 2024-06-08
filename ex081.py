valores = []

while True:
    valores.append(int(input("Digite um valor: ")))

    continuar ="A"
    while continuar not in "SN":
        continuar = input("Deseja continuar? [S/N]").strip().upper()[0]
    
    if continuar == "N":
        break

print("=-" * 30)
print(f"Você digitou {len(valores)} valores")
valores.sort(reverse=True)
print("Os valores em ordem decrescente são", end=" ")
for valor in valores:
    print(valor, end=" ")
print("\nO valor 5 faz parte da lista!" if 5 in valores else "\nO valor 5 não está na lista!")