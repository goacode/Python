from datetime import datetime

ano = int(input("Digite um ano qualquer (Ou 0 para o ano atual)\n"))
if ano == 0:
    ano = datetime.now().year


if ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto!")

else:
    print(f"{ano} não é um ano bissexto!")