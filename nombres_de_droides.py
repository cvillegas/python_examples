"""
Generar 100 nombres distintos de droides de Star Wars

Bajo las siguientes reglas:

* Todos los nombres tienen dos partes separadas por un guión
* La primera parte tiene dos caracteres
* El primer caracter de la primera parte siempre es una letra
* Para la segunda partes hay 4 patrones distintos
* El primer patrón de la segunda parte está formado por dos letras (Ej. C3-PO)
* El segundo patrón de la segunda parte está formado por una letra y un número (Ej. R2-D2) 
* El segundo patrón de la segunda parte está formado por un solo número (Ej. BB-8)
* El tercer patrón de la segunda parte está formado por dos números (Ej. IG-99)
"""
from pprint import pprint
from string import digits, ascii_uppercase
from random import randint, choice

NUMERO_DROIDES = 100

droides = []

# L - Letra  / N - Número / A - Ambos
PATRONES_PARTE_1 = ['LA']
PATRONES_PARTE_2 = ['LL', 'LN', 'N', 'NN']

while (len(droides) < NUMERO_DROIDES):

    #nombre = []
    nombre = ''
    patron = choice(PATRONES_PARTE_1)

    for c in patron:
        if c == 'L':
            nombre += choice(ascii_uppercase)
        elif c == 'A':
            nombre += choice(digits + ascii_uppercase)

    nombre += '-'

    patron = choice(PATRONES_PARTE_2)
    for c in patron:
        if c == 'L':
            nombre += choice(ascii_uppercase)
        elif c == 'N':
            nombre += choice(digits)
        elif c == 'A':
            nombre += choice(digits + ascii_uppercase)

    #nombre = ''.join(nombre)

    if nombre not in droides:
        droides.append(nombre)

pprint(droides)
