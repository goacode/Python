print("=" * 30)
print(" " * 3, "10 Termos de uma PA" ," " * 3)
print("=" * 30)

primeiro_termo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))


for c in range (primeiro_termo, ((primeiro_termo + razao * 9) + 1), razao):
    print(f"{c}", end=" => ")

print("FIM")