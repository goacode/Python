soma = numeros = 0

while True:

    numero = int(input("Digite um valor (999 para parar): "))
    if numero == 999:
        break

    soma += numero
    numeros += 1

print(f"A soma dos {numeros} valores foi {soma}!")