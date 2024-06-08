impares = []
pares = []
numeros = []

while True:
    valor = int(input("Digite um número: "))
    numeros.append(valor)
    pares.append(valor) if valor % 2 == 0 else impares.append(valor)

    r = "A"
    while r not in "SN":
        r = input("Deseja continuar? [S/N]").strip().upper()[0]
    
    if r == "N":
        break

print(f"Os números digitados foram: {numeros}")
print(f"Os números pares digitados foram: {pares}")
print(f"Os números impares digitados foram: {impares}")


