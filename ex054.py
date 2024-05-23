from datetime import datetime
maioridade = menoridade = 0
for i in range(1, 8):
    ano = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1

print(f"Ao todos tivemos {maioridade} pessoas maiores de idade")
print(f"e tambem tivemos {menoridade} pessoas menores de idade.")