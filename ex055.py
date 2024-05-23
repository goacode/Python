pesos = []
for i in range(1, 6):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    pesos.append(peso)

print(f"O maior peso lido foi de {max(pesos)}kg")
print(f"O menor peso lido foi de {min(pesos)}kg")