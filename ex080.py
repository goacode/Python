valores = []
for cont in range(0, 5):
    valor = int(input("Digite um valor: "))
    if cont == 0 or valor > valores[len(valores) - 1]:
        valores.append(valor)
        print("Valor adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(valores):
            if valor <= valores[pos]:
                valores.insert(pos, valor)
                print(f"Valor adicionado na posição {pos}")
                break
            pos += 1

print("=-" * 30)
print(valores)

    
