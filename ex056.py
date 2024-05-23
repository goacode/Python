idades_soma = 0
maior_idade = 0
mulheres_jovens = 0

for i in range(1, 5):
    print("-" * 5, f"{i} PESSOA", "-" * 5)
    nome = input("Nome: ").strip().title()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    idades_soma += idade
    if sexo == "M" and idade > maior_idade:
        nome_do_velho = nome
        maior_idade = idade

    elif sexo == "F" and idade < 20:
        mulheres_jovens += 1

media_idade = idades_soma / 4

print(f"A média de idade do grupo é de {media_idade} anos.")
print(f"O homem mais velho tem {maior_idade} e se chama {nome_do_velho}.")
print(f"Ao todo são {mulheres_jovens} mulheres com menos de 20 anos.")
