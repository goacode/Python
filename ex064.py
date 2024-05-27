n_numeros = 0
soma = 0
numero = int(input("Digite um numero [999 para parar]: "))
while numero != 999:
    soma += numero
    n_numeros += 1
    numero = int(input("Digite um numero [999 para parar]: "))
print(f"Você digitou {n_numeros} numeros e a soma entre eles foi {soma}.")