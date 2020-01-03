import string
from random import choice

ALFABETO = string.digits + string.ascii_uppercase
NUM_LICENCIAS = 100
NUM_GRUPOS = 5
NUM_CARACTERES = 5

def genera_grupo(num_caracteres=NUM_CARACTERES):
    grupo=[]
    for n in range(num_caracteres):
        grupo.append(choice(ALFABETO))
    return ''.join(grupo)


def genera_licencia(num_grupos=NUM_GRUPOS):
    licencia=[]
    for n in range(num_grupos):
        licencia.append(genera_grupo())
    return '-'.join(licencia)


def generar_n_licencias(numero=NUM_LICENCIAS):
    lista_licencias = []
    while len(lista_licencias) < numero:   
        lista_licencias.append(genera_licencia())
    return lista_licencias

if __name__ == "__main__": 

    lista_licencias = sorted(generar_n_licencias())
    print(lista_licencias)
    for nro, licencia in enumerate(lista_licencias, 1):
        print(f"{nro:03d}.- {licencia}")