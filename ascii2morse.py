ASCII_TO_MORSE = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '?': '..--..',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
 }

CARACTERES_VALIDOS = list(ASCII_TO_MORSE.keys()) + [' ']

cadena = input("Ingrese una cadena: ")

ok = True
for c in cadena.upper():
    if c not in CARACTERES_VALIDOS:
        ok = False
        break

if not ok:
    print("ERROR: Solo dígitos, letras mayúsculas del idioma inglés y espacios en blanco")

partes = []
for c in cadena.upper():
    if c == ' ':
        partes.append(c)
    else:
        partes.append(ASCII_TO_MORSE[c])

print(" ".join(partes))
