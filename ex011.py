comprimento = float(input("Insira o comprimento da parede: "))
largura = float(input("Insira a largura da parede: "))
area = largura * comprimento 
tinta = area/2

print(f"Será necessario {tinta:.2f}L de tinta para pintar a parede")