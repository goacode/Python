numero = (input("Informe um número: "))

print(f"Numero = {numero}")
print(f"Unidade: {numero[-1]}")
print(f"Dezena: {numero[-2]}")
print(f"Centena: {numero[-3]}")
print(f"Milhar: {int(numero)//1000}")
