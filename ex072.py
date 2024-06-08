extenso = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez",
           "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
numero = int(input("Digite um número entre 0 e 20: "))

while numero > 20 or numero < 0:
    numero = int(input("[ERRO] Digite um número entre 0 e 20: "))

print(f"Você digitou o número {extenso[numero]}")

