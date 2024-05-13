velocidade = float(input("Insira a velocidade do carro (km/h)\n "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado em R${multa:.2f}")

else: 
    print("Bom Dia! Prossiga com cautela.")

