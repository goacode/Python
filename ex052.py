numero = int(input("Digite um numero: "))
divisores = 0
for c in range(1,numero + 2):
    if numero % c == 0:
        print(f"\033[1;32;40m{c}", end=" ")
        divisores += 1
    else:
        print(f"\033[1;33;40m{c}", end=" ")

print(f"O numero {numero} foi divisivel {divisores}x")
if divisores != 2:
    print("E por isso ele NÃO é primo!")

else:
    print("E por isso ele É primo")

    
