print("=" * 30)
print(" " * 3, "10 Termos de uma PA" ," " * 3)
print("=" * 30)
cont = 10
termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
n_termos = 0
while cont != 0:
    print(f"{termo}", end=" => ")
    termo += razao
    n_termos += 1

    if cont == 1:
        print("PAUSA")
        cont = int(input("\nQuantos termos deseja mostrar a mais? ")) + 1 if cont != 0 else + 0
    cont -= 1
print(f"Progressão finalizada com {n_termos} termos mostrados.")
    