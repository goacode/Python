from datetime import datetime
nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}")
if idade < 18:
    print(f"Faltam {18 - idade} anos para seu alistamento")
    print(f"Seu alistamento sera em {(18 - idade) + ano_atual}")

elif idade == 18:
    print(f"Você tem {idade} anos")
    print("Deve se alistar imediatamente")

else:
    print(f"Você deveria ter se alistado a {(ano_atual - nascimento) - 18} anos")
    print(f"Seu alistamento foi em {nascimento + 18}")

