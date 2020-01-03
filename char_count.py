import string

contadores = {}

for letra in string.ascii_uppercase:
    contadores[letra] = 0

cadena = input("Ingrese una cadena: ")

for c in cadena:
    c = c.upper()
    if c in contadores:
        contadores[c] += 1

print("Frecuencias:\n")

for letra in string.ascii_uppercase:
    print(f"Letra: {letra} Veces: {contadores[letra]}")
