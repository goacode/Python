from random import randint
from time import sleep
print("=" * 5, "JOKENPOO!", "=" * 5)
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")
objetos = ["Pedra", "Papel", "Tesoura"]
jogada = int(input("Qual é a sua jogada? "))
computador = randint(1, 3)

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("POO!")
sleep(0.5)

print("=-" * 10, end="= \n")   
print(f"O computador jogou {objetos[computador - 1]}")
print(f"O jogador jogou {objetos[jogada - 1]}")
print("=-" * 10, end="= \n") 

if jogada == 1:
    if computador == 1:
        print("É UM EMPATE!")

    if computador == 2:
        print("O COMPUTADOR VENCE!!!")

    if computador == 3:
        print("O jogador venceu...")

elif jogada == 2:
        
    if computador == 1:
        print("O jogador venceu...")

    if computador == 2:
        print("É UM EMPATE!")

    if computador == 3:
        print("O COMPUTADOR VENCE!!!")

elif jogada == 3:
    
    if computador == 1:
        print("O COMPUTADOR VENCE!!!")

    if computador == 2:
        print("O jogador venceu...")

    if computador == 3:
        print("É UM EMPATE!")

else: 
    print("[ERRO] Opção Invalida! Tente novamente.")



