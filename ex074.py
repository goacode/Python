from random import randint

valores = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)

print("Os valores sorteados foram: ", end="")
for valor in valores:
    print(valor, end=" ")

print("")
print(f"O maior valor sorteado foi {max(valores)}")
print(f"O menor valor sorteado foi {min(valores)}")