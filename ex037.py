numero = int(input("Digite um numero inteiro: "))
print("Escolha uma das seguintes bases para conversão")
print("[1] BINÁRIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")
opcao = input("Escolha: ")

if opcao == "1":
    print(f"{numero} convertido para binário: {bin(numero)[2:]}")
    
elif opcao == "2":
    print(f"{numero} convertido para octal: {oct(numero)[2:]}")
    
elif opcao == "3":
    print(f"{numero} convertido para hexadecimal: {hex(numero)[2:]}")
    
else:
    print("Opção Invalida!")
