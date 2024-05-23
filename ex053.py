frase = input("Digite uma frase:").strip()
frase_reversa = frase[::-1]


if frase == frase_reversa:
    print("É um palindromo!")

else:
    print("Não é um palindromo!")