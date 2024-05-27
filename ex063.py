termos = int(input("Quantos termos você deseja mostrar? "))
cont = termos
termo1 = 0
termo2 = 1
while cont > 0:

    if cont == termos:
        print(f"{termo1}", end=" => ")
    elif cont == termos - 1:
        print(f"{termo2}", end=" => ") 

    else:
        fibonacci = termo1 + termo2
        print(f"{fibonacci}", end=" => ")
        termo1 = termo2
        termo2 = fibonacci
    cont -= 1
print("FIM")
    