a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print("É possivel formar o triangulo com essas medidas!")

else:
    print("É impossivel formar o triangulo com essas medidas!")