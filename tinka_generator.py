# Name: tinka_generator.py
# Version: 0.3
# Author: Cesar Villegas Ureta - https//www.slayerx.org/
# GitHub repo: https://github.com/cvillegas/python_examples
# License: MIT License
# Description: Generador de jugados de la lotería peruana "La Tinka"

import json
from random import sample
from pprint import pprint
BOLILLA_INICIAL = 1
BOLILLA_FINAL = 45

BOLILLAS_POR_JUGADA = 6

BOLILLAS = tuple(range(BOLILLA_INICIAL, BOLILLA_FINAL + 1))

# Solicitar el número de jugadas, si se orden y si se guarda en un archivo


NUM_JUGADAS = int(input("Ingrese el nro de jugadas: "))

ORDEN = input("¿Desea ordenar las jugadas? (S/N): ")

GRABAJSON = input("¿Desea grabar sus jugadas en un archivo json? (S/N): ")


lista_jugadas = []

while len(lista_jugadas) < NUM_JUGADAS:

    jugada = sample(BOLILLAS, BOLILLAS_POR_JUGADA)
    jugada.sort()

    partes = []
    for b in jugada:
        partes.append("%02d" % b)
    jugada_como_cadena = '-'.join(partes)

    if jugada_como_cadena not in lista_jugadas:
        lista_jugadas.append(jugada_como_cadena)

if str.lower(ORDEN) == "s" or str.lower(ORDEN) == "y":
    lista_jugadas.sort()


for nro, jugada in enumerate(lista_jugadas, 1):
    print(f"{nro:5d} -> {jugada}")


if str.lower(GRABAJSON) == "s" or str.lower(GRABAJSON) == "y":
    fp = open('jugadas-tinka.json', 'w+')
    fp.write(json.dumps(lista_jugadas, indent=4))
    fp.close()

    print("\n Sus jugadas se encuentran en el archivo: jugadas-tinka.json")

