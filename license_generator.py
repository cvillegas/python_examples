import string
from random import choice

NUM_LICENCIAS = 100
NUM_GRUPOS = 5
NUM_CARACTERES_EN_GRUPO = 5

ALFABETO = string.digits + string.ascii_uppercase

lista_licencias = []

while len(lista_licencias) < NUM_LICENCIAS:
    
    grupos = []
    for n in range(NUM_GRUPOS):
        caracteres = []
        for n in range(NUM_CARACTERES_EN_GRUPO):
            caracteres.append(choice(ALFABETO))
        grupos.append( ''.join(caracteres ))
    licencia = '-'.join(grupos)
    
    if licencia not in lista_licencias:
        lista_licencias.append(licencia)

lista_licencias.sort()

for nro, licencia in enumerate(lista_licencias, 1):
    print(f"{nro:03d}.- {licencia}")
