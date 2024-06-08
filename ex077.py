palavras = (
    'Sol', 'Árvore', 'Carro', 'Montanha', 'Computador',
    'Rio', 'Praia', 'Livro', 'Janela', 'Telefone',
    'Cachorro', 'Gato', 'Casa', 'Relógio', 'Mesa',
    'Cadeira', 'Caneta', 'Estrela', 'Bola', 'Fogo'
)

vogais = ("A","Á","Ã","Â", "E", "É", "Ê", "I", "Í" "O", "Ó" "Ô","Õ", "U", "Ú")

for palavra in palavras:
    print(f"\nNa palavra {palavra} temos", end=" ")
    for letra in palavra:
        if letra.upper() in vogais:
            print(letra, end=" ")