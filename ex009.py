numero = int(input("Insira um numero: "))
repeticoes = int(input("Insira o numero de repetições: "))

while repeticoes > 0:
    print(f"{numero} x {repeticoes} = {numero * repeticoes}")
    repeticoes -= 1