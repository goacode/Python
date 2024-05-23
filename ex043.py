from math import pow
peso = float(input("Qual seu peso? (kg) "))
altura = float(input("Qual sua altura? (m) "))
imc = peso / pow(altura, 2)

print(f"O IMC dessa pessoa é de {imc:.2f}")

if imc < 18.5:
    print("Você esta abaixo do peso, precisa comer feijão!")

elif imc < 25:
    print("Você esta na faixa de peso normal, continue assim!")

elif imc < 30:
    print("Você esta com sobrepeso, amigo vamos fazer uma dieta.")

elif imc < 40:
    print("Você está em obesidade, quadro preocupante!")

else:
    print("Você esta em obesidade morbida, precisa de tratamento urgente!")
