from random import randint
print("Olá, humano!")
print("Vamos jogar um jogo tente adivinhar um numero entre 0 e 10.")
tentativas = 0
computador = randint(0, 10)
palpite = int(input("Qual seu palpite? "))
while palpite != computador:
    if palpite > computador:
        palpite = int(input("Menos, tente outra vez.\n"))
    else:
        palpite = int(input("Mais, tente outra vez.\n"))
    tentativas += 1

print(f"Parabéns você acertou apos {tentativas} tentativas!")
