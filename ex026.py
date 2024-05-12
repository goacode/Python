nome = input("Digite uma frase: ").strip().lower()

print(f"A Letra A apareceu {nome.count('a')}x na frase") 
print(f"A primeira letra A aparece na posição {nome.find('a') + 1}")
print(f"A primeira letra A aparece na posição {nome.rfind('a') + 1}")