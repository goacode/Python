from os import system
opcao = 0
n1 = float(input("Primeiro numero: "))
n2 = float(input("Segundo numero: "))
while opcao != "5":

    opcao = input("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do Programa
    """)

    if opcao == "1":
        print(f"A soma entre {n1} e {n2} é {n1 + n2}!")
    
    elif opcao == "2":
        print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}!")

    elif opcao == "3":
        if n1 > n2:
            print(f"{n1} é o maior numero.")

        else:
            print(f"{n2} é o maior numero.")

    elif opcao == "4":
        print("Informe os numeros novamente.")
        n1 = float(input("Primeiro numero: "))
        n2 = float(input("Segundo numero: "))
        
    elif opcao == "5":
        print("Desligando...")

    else:
        print("Opção Invalida tente novamente!")
        opcao = input("""
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Numeros
        [5] Sair do Programa
        """)

    input("(Aperte ENTER para continuar)")
    system("cls")



