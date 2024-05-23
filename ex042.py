n1 = float(input("Primeiro Segmento: "))
n2 = float(input("Segundo Segmento: "))
n3 = float(input("Terceiro Segmento: "))
verdades = sum([n1 == n2, n1 == n3, n2 == n3])

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    if verdades == 0:
        print("Os segmento acima podem formar um triangulo ESCALENO")
    
    elif verdades == 1:
        print("Os segmentos acima podem formar um triangulo ISÓCELES")

    else:
        print("Os segmentos acima podem formar um triangulo EQUILATERO")

else:
    print("Não é possivel formar um triangulo com os segmentos acima!")