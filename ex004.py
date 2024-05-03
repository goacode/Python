entrada = input("Digite algo: ")
print(f"Entrada: {entrada}")
print(f"Tipo Primitivo: {type(entrada)}\n")

print("================================\n")

print(f"É um numero? {entrada.isnumeric()}")
print(f"É alfabetico? {entrada.isalpha()}")
print(f"É alfanumerico? {entrada.isalnum()}")
print(f"Esta em maiusculo? {entrada.isupper()}")
print(f"Esta em minusculo? {entrada.islower()}")
print(f"Esta capitalizado? {entrada.istitle()}")
print(f"É apenas espaço? {entrada.isspace()}")
  
  