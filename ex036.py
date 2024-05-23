valor_casa = float(input("Insira o valor do imovel: "))
salario = float(input("Insira o salario do comprador: "))
prazo = int(input("Insira o prazo do pagamento em anos: "))

mensalidade = valor_casa / (prazo * 12)

if mensalidade > (salario * 0.3):
    print(f"O valor da prestação será R${mensalidade:.2f}, emprestimo negado!")
else:
    print(f"O valor da prestação será R${mensalidade:.2f}, emprestimo concedido.")
        