valores = (
    int(input("Digite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: "))
)
pares = []

print("Você digitou os valores: ", end="")
for valor in valores: 
    print(valor, end=" ")
    if valor % 2 == 0:
        pares.append(valor)
    
if 9 in valores:
    print(f"\nO valor 9 apareceu {valores.count(9)} veze(s)")
else:
    print("\nNenhum 9 foi digitado!")

if 3 in valores:
    print(f"O valor 3 apareceu na posição {valores.index(3) + 1}")
else:
    print("Nenhum 3 foi digitado!")

if len(pares) > 0:
    print(f"Os valor(es) par(es) digitad(os) foram", end=" ")
    for valor in pares:
        print(valor, end=" ")
else:
    print("Não foram digitados números pares!")
