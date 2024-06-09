from random import randint
from time import sleep
print("=" * 30)
print(f"{"MEGA SENA":^30}")
print("=" * 30)

numero_jogos = int(input("Você gostaria de sortear quantos jogos? "))
jogos = []
jogo = []

for cont in range(0, numero_jogos):
    for i in range(1, 7):
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
    
    jogos.append(jogo[:])
    jogo.clear()

for pos, jogada in enumerate(jogos):
    sleep(0.5)
    print(f"Jogo {pos+1}: {jogada}")

