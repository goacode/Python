produtos = (
    'Detergente', 2.50,
    'Desinfetante', 3.75,
    'Sabão em pó', 8.90,
    'Água sanitária', 2.10,
    'Esponja', 1.50,
    'Limpador multiuso', 5.20,
    'Desengordurante', 6.30,
    'Amaciante', 7.45,
    'Saco de lixo', 4.00,
    'Vassoura', 9.80
)

print("=" * 40)
print(f"{"LOJÃO DA DONA SILVÍA":^30}")
print("=" * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}", end="")

    else:
        print(f"R${produtos[pos]:>5.2f}")