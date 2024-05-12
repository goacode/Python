nome = input("Digite seu nome completo: ")
nome_token = nome.split()
letras_totais = 0
for palavras in nome_token:
    for letras in palavras:
        letras_totais += 1

print(f"Olá, {nome}")
print(f"Maiusculas: {nome.upper()}")
print(f"Minusculas: {nome.lower()}")
print(f"Letras Primeiro Nome: {len(nome_token[0])}")
print(f"Letras totais: {letras_totais}")

