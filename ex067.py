while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))
    print("=" * 25)

    if valor < 0:
        break
    cont = 1
    while cont <= 10:
        print(f"{valor} x {cont} = {valor * cont}")
        cont += 1

    print("=" * 25)

print("Programa Encerrado!")