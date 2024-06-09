valores = [[], [], []]
for cont in range(0, 3):
    for i in range(0, 3):
        valores[cont].append(int(input(f"Digite um valor para a posição [{cont}, {i}]: ")))

print("=-=" * 20)
for linha in valores:   
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
    print("")