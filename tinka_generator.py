import json
from random import sample
from pprint import pprint
BOLILLA_INICIAL = 1
BOLILLA_FINAL = 45

BOLILLAS_POR_JUGADA = 6

BOLILLAS = tuple(range(BOLILLA_INICIAL, BOLILLA_FINAL + 1))

NUM_JUGADAS = 100

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

lista_jugadas.sort()

for nro, jugada in enumerate(lista_jugadas, 1):
    print(f"{nro:05d}.- {jugada}")

fp = open('jugadas-tinka.json', 'w+')
fp.write(json.dumps(lista_jugadas, indent=4))
fp.close()