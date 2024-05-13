maior = menor = float(input("Primero valor: "))
n2 = float(input("Segundo valor: "))
n3 = float(input("Terceiro valor: "))

if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print(f"{maior} foi o maior valor digitado")
print(f"{menor} foi o menor valor digitado")