inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
s = 0

for c in range (inicio, fim + 1):
    if c % 3 == 0 and c % 2 == 0:
        s += c
    
print(f"A soma é {s}!")