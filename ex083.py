expressao = input("Digite sua expressão: ")
abre = expressao.count("(")
fecha = expressao.count(")")
print("Sua expressão é valida" if fecha == abre else "Sua expressão está errada")
