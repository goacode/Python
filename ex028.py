from random import randint

numero = randint(0, 5)

entrada = int(input("Tente adivinhar o número entre 0 e 5!\n"))

if numero == entrada:
    print("Você venceu!")
else:
    print(f"Você perdeu! O número certo era {numero}.")

