distancia = float(input("Qual a distancia da sua viagem em km/h? "))

if distancia > 200:
    preco = distancia * 0.45
    print(f"Sua viagem custara R${preco:.2f}")

else:
    preco = distancia * 0.5
    print(f"Sua viagem custara R${preco:.2f}")