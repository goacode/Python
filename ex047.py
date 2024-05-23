inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

for c in range (inicio, fim + 1):
    if c % 2 == 0:
        print(c)