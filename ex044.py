print("=" * 5, " LOJAS CASSANDRA ", "=" * 5)
compras = float(input("Total das compras: R$"))
print("Formas de pagamento")
print("[1] À vista (Dinheiro/Cheque)")
print("[2] À vista Cartão")
print("[3] 2x no Cartão")
print("[4] 3x ou mais no Cartão")
opcao = input("Qual sua opção? ")

if opcao == "1":
    print(f"Suas compras de R${compras:.2f} saira por R${(compras * 0.9):.2f} após os descontos!")

elif opcao == "2":
    print(f"Suas compras de R${compras:.2f} saira por R${(compras * 0.95):.2f} após os descontos!")

elif opcao == "3":
    print(f"Suas compras sairão por R${compras:.2f} SEM JUROS com cada parcelando custando R${(compras/2):.2f}")

elif opcao == "4":
    parcelas = int(input("Quantas parcelas? "))
    compras = compras * 1.2
    print(f"Suas compras sairão por R${compras:.2f} com parcelas de R${compras/parcelas:.2f}")

else:
    print("[ERRO] OPÇÃO INVALIDA!")
