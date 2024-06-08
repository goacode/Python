times_brasileirao= (
    "Fluminense",
    "Bahia",
    "Atlético-MG",
    "Botafogo",
    "São Paulo",
    "Internacional",
    "Chapecoense",
    "Palmeiras",
    "Corinthians",
    "Cuiabá",
    "Cruzeiro",
    "Fortaleza",
    "Athletico-PR",
    "América-MG",
    "Vasco da Gama",
    "Red Bull Bragantino",
    "Grêmio",
    "Coritiba",
    "Santos",
    "Flamengo"
)

print("Lista de times do brasileirão: ", end='')
for time in times_brasileirao:
    print(f"{time},", end=" ")

print("")
print("-=" * 20)

print("Os 5 primeiros são: ", end="")
for time in range(0,6):
    print(f"{times_brasileirao[time]},", end=" ")

print("")
print("-=" * 20)

print("Times em ordem alfabética: ", end="")
for time in sorted(times_brasileirao):
    print(f"{time}, ", end="")

print("")
print("-=" * 20)

print(f"A Chapecoense está em {times_brasileirao.index("Chapecoense") + 1}º Lugar")



