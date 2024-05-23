from emoji import emojize
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

print(f"Tirando {n1} e {n2} sua média sera {media}")

if media >= 7:
    print(emojize("O aluno está aprovado! :polegar_para_cima:", language='pt'))

elif media >= 5:
    print(emojize("O aluno esta de recuperação. 🙏"))

else:
    print(emojize("O aluno está reprovado! :polegar_para_baixo:", language='pt'))