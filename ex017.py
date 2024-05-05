from math import hypot
c_oposto = float(input("Comprimento do cateto oposto: "))
c_adj = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(c_oposto, c_adj)

print(f"A hipotenusa vai medir {hipotenusa}")