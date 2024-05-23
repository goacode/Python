soma = 0
quant_numeros = 0
for i in range(0, 6):
    numero = int(input("Digite um numero inteiro: "))
    if numero % 2 == 0:
        soma += numero
        quant_numeros += 1
print(f"Você informou {quant_numeros} número(s) par(es) e a soma deles é {soma}!")