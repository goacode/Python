velocidade = float(input("Insira a velocidade do carro (km/h)\n "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"\033[1;31;40mVocê foi multado em R${multa:.2f}!")

else: 
    print("\033[1;31;43mBom Dia! Prossiga com cautela.")

