valores = [
    [], 
    []
]

for cont in range(1, 8):
    num = int(input(f"Digite o {cont}º valor: "))

    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)

valores[0].sort()
valores[1].sort()
print(f"Valores pares {valores[0]}")
print(f"Valores impares {valores[1]}")
