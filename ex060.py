numero = int(input("Digte um numero para calcular seu fatorial\n"))
fatorial = 1
print(f"Calculando {numero}!", end=" = ")
while numero > 0:
    print(f"{numero} ", end="")
    print(f"x " if numero > 1 else "= ", end="")
    fatorial *= numero
    numero -= 1
print(fatorial)
