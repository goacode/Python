print("=" * 30)
print(" " * 3, "10 Termos de uma PA" ," " * 3)
print("=" * 30)
cont = 10
termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))

while cont > 0:
    print(f"{termo}", end=" => ")
    termo += razao
    cont -= 1
print("FIM")