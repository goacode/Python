valores = [
    [], 
    [], 
    []
]
soma_pares = soma_coluna = 0
for cont in range(0, 3):
    for i in range(0, 3):
        valores[cont].append(int(input(f"Digite um valor para a posição [{cont}, {i}]: ")))

print("=-=" * 20)
for linha in valores:
    print("")
    soma_coluna += linha[2]
    for valor in linha:
        print(f"[{valor:^5}]", end=" ")
        if valor % 2 == 0:
            soma_pares += valor
      
print("")
print("=-=" * 20)
print(f"A soma de todos os valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_coluna}")
print(f"O maior valor da segunda linha é {max(valores[1])}")
