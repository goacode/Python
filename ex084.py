pessoas = list()
dados = list()

while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        elif dados[1] < menor_peso:
            menor_peso = dados[1]

    r = "A"
    while r not in "SN":
        r = input("Deseja continuar? [S/N]").strip().upper()[0]
    if r == "N":
        break

    dados.clear()
print("=-=" * 15)
print(f"Você cadastrou {len(pessoas)} pessoas!")

print(f"O maior peso foi de {maior_peso:.1f}kg, de ", end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}]", end=" ")

print(f"\nO menor peso foi de {menor_peso:.1f}kg, de ", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}]", end=" ")