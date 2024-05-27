continuar = "S"
valores = []
while continuar == "S":
    numero = int(input("Digite um numero: "))
    valores.append(numero)
    continuar = input("Quer continuar [S/N] ").upper().strip()

print(f"Você digitou {len(valores)} numero(s) e a media foi {sum(valores)/len(valores)}")
print(f"O maior valor foi {max(valores)} e o menor foi {min(valores)}")