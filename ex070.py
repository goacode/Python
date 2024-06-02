total_compra = caros = 0
print("""
--------------------------------
      Loja Super Baratão
--------------------------------
""")
while True:
    nome = input("Nome do Produto:").title()
    preco = float(input("Preço: R$"))

    if total_compra == 0 or preco < preco_barato:
        produto_barato = nome
        preco_barato = preco

    total_compra += preco

    if preco > 1000:
        caros += 1
    
    continuar = "a"
    while continuar not in "SN": 
        continuar = input("Quer continuar? [S/N]").strip().upper()[0]

    if continuar == "N":
        break

print("---------- FIM DO PROGRAMA ------------")
print(f"O total da compra foi R${total_compra:.2f}")
print(f"Temos {caros} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produto_barato} que custa R${preco_barato:.2f}")
