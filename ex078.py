valores = []
p_menor = []
p_maior = []

for pos in range(0,5):
    numero = int(input(f"Digite um valor para a posição {pos}: "))
    valores.append(numero)

for pos, valor in enumerate(valores):
    if valor == max(valores):
        p_maior.append(pos)
    elif valor == min(valores):
        p_menor.append(pos)

print("Você digitou os valores", end=' ')
for valor in valores:
    print(valor, end=" ")

print(f"\nO maior valor digitado foi {max(valores)}, nas posições", end=" ")
for pos in p_maior:
    print(f"{pos}", end="... ")

print(f"\nO menor valor digitado foi {min(valores)}, nas posições", end=" ")
for pos in p_menor:
    print(f"{pos}", end="... ")
