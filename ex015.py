dias = int(input("Insira a quantidade de dias alugados: "))
quilometragem = float(input("Insira a quantidade de KM rodados: "))

total = (dias * 60) + (quilometragem * 0.15)

print(f"Total a pagar: R${total:.2f}")