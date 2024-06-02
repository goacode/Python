maiores = homens = mulheres_jovens = 0

while True:
    sexo = "A"
    print("Cadastre uma pessoa")
    print("-" * 20)
    idade = int(input("Idade: "))

    while sexo not in "MF":
        sexo = input("Sexo: [M/F]").strip().upper()[0]

    if idade > 17:
        maiores += 1

    if sexo == "M":
        homens += 1
    
    if sexo == "F" and idade < 20:
        mulheres_jovens += 1

    print("-" * 20)
    continuar = "A"
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    print("-" * 20)

    if continuar == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {maiores}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres_jovens} mulheres com menos de 20 anos")

