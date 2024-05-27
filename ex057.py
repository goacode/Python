sexo = input("Informe seu sexo [M/F]\n").upper().strip()
while sexo != "M" and sexo != "F":   
    sexo = input("Dados Inválidos! Informe seu sexo: ").upper().strip()
print(f"Sexo {"Feminino" if sexo == "F" else "Masculino"} registrado com sucesso!")
