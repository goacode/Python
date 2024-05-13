from random import randint

numero = randint(0, 5)

entrada = int(input("\033[1;34;40mTente adivinhar o número entre 0 e 5!\n"))

if numero == entrada:
    print("\033[1;32;40mVocê venceu!")
else:
    print(f"\033[1;31;40mVocê perdeu! O número certo era {numero}.")

