from random import choice
from string import (
    digits,
    ascii_uppercase
)

NUM_PLACAS = 20

PLANTILLAS = [
    'LL-NNNN',
    'LLL-NNN',
    'LNL-NNN'
]

lista_placas = []

while len(lista_placas) < NUM_PLACAS:
        
    plantilla = choice(PLANTILLAS)

    partes = []
    for c in plantilla:
        if c == 'L':
            partes.append(choice(ascii_uppercase))
        elif c == 'N':
            partes.append(choice(digits))
        else:
            partes.append(c)

    placa = ''.join(partes)

    if placa not in lista_placas:
        lista_placas.append(placa)

for nro, placa in enumerate(lista_placas, 1):
    print(f"{nro:04d}.- {placa}")