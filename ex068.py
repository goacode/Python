from random import randint

print("=-" * 30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-" * 30)
vitorias = 0

while True:
 
    usuario = int(input("Diga um valor: "))
    escolha = input("Par ou Impar? [P/I]").strip().upper()
    computador = randint(0,10)
    total = usuario + computador
    resultado = "P" if total % 2 == 0 else "I"
    print("-" * 25)
    print(f"Você jogou {usuario} e o computador {computador}. Total de {total} deu {"PAR" if resultado == "P" else "IMPAR"}")
    print("-" * 25)
    
    if escolha == resultado:
        print("Você venceu!")
        print("Vamos jogar Novamente...")
        print("=-" * 30)
        vitorias += 1
    else:
        print("Você perdeu!")
        print("=-" * 30)
        print(f"GAME OVER! você venceu {vitorias} veze(s)")
        break
