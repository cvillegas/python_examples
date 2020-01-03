"""
Ud. deberá utilizar 7 banderas para hacer seguiento
del estado de las siguientes variables:

- Si estan contando personas mayores ó menores de edad
- Si se están contando personas de género masculino ó femenino
- Si se están contando personas de la capital u otras ciudades
- Si ya se terminó de contar personas por edad
- Si ya se terminó de contar personas por género
- Si ya se terminó de contar personas por lugar de procedencia
- Si ya se terminó con las 3 búsquedas

- Deberán contarse 3 personas menores de edad antes de empezar
  a contar 3 personas mayores de edad
- Deberán contarse 5 personas de género masculino antes de empezar
  a contar 5 personas de género femenino
- Deberan contarse 10 personas de la capital antes de empezar a
  contar 10 personas de otras ciudades

En todo momento, la salida deberá indicar en que estado esta cada
una de las banderas, por ejemplo:

edad: menores 
género: masculino
procedencia: capital

busqueda por edad: completada
búsqueda por género: en curso
búsqueda por lugar de procedencia: en curso

El programa generará una tripleta de datos aleatoriamente,
como por ejemplo:

(13, 'M', 'Arequipa')
(65, 'F', 'Lima)
(13, 'M', 'Ica')
"""

from time import sleep
from random import (
    randint,
    choice
)

PAUSA = 1.0 # segundos

INICIO_RANGO_EDAD = 0
FIN_RANGO_EDAD = 80

LONGITUD_VUELTA_EDAD = 3
LONGITUD_VUELTA_GENERO = 5
LONGITUD_VUELTA_PROCEDENCIA = 10

MAYORIA_DE_EDAD = 18

OPCIONES_EDAD = ('menores', 'mayores')
OPCIONES_PROCEDENCIA = ('capital', 'otra ciudad')

GENEROS = ('M', 'F')
LUGARES = ('Piura', 'Chiclayo', 'Ancash', 'Lima', 'Ica', 'Arequipa', 'Tacna')

CAPITAL = 'Lima'

buscando_edad = OPCIONES_EDAD[0]
buscando_genero = GENEROS[0] 
buscando_procedencia = OPCIONES_PROCEDENCIA[0]

busqueda_por_edad_completa = False
busqueda_por_genero_completa = False
busqueda_por_procedencia_completa = False
busqueda_completa = False

contador_edad = 0
contador_genero = 0
contador_procedencia = 0

while not busqueda_completa:

    edad = randint(INICIO_RANGO_EDAD, FIN_RANGO_EDAD)
    genero = choice(GENEROS)
    lugar = choice(LUGARES)

    tripleta = (edad, genero, lugar)

    # Detectar cambios
    if edad >= MAYORIA_DE_EDAD:
        grupo_edad_encontrada = 'mayores'
    else:
        grupo_edad_encontrada = 'menores'

    # Detecto el evento en donde debería contar
    if (not busqueda_por_edad_completa) and (buscando_edad == grupo_edad_encontrada):
        contador_edad += 1

        # Existe la posibilidad de que se llegue
        # al valor máximo del contador
        # También la posibilidad de que se haya concluido todas las vueltas
        if contador_edad == LONGITUD_VUELTA_EDAD:
            if buscando_edad == OPCIONES_EDAD[0]:
                buscando_edad = OPCIONES_EDAD[1]
                contador_edad = 0
            else:
                busqueda_por_edad_completa = True

    if genero == GENEROS[0]:
        grupo_genero_encontrado = "M"
    else:
        grupo_genero_encontrado = "F"

    if (not busqueda_por_genero_completa) and (buscando_genero == grupo_genero_encontrado):
        contador_genero += 1 

        if contador_genero == LONGITUD_VUELTA_GENERO:
            if buscando_genero == GENEROS[0]:
                buscando_genero = GENEROS[1]
                contador_genero = 0
            else:
                busqueda_por_genero_completa = True
 

    
    if(not busqueda_por_procedencia_completa):
        if(lugar == CAPITAL):
            contador_procedencia +=1
            if(contador_procedencia == LONGITUD_VUELTA_PROCEDENCIA):
                busqueda_por_procedencia_completa = True




    print(tripleta)
    print()
    print("edad: {}".format(buscando_edad))
    print("género: {}".format('masculino' if buscando_genero == 'M' else 'femenino'))
    print("procedencia: {}".format(buscando_procedencia))
    print()
    print("busqueda por edad: {}".format('completa' if busqueda_por_edad_completa else 'en curso'))
    print("busqueda por género: {}".format('completa' if busqueda_por_genero_completa else 'en curso'))
    print("busqueda por procedencia: {}".format('completa' if busqueda_por_procedencia_completa else 'en curso'))
    print()
    print("contador edad: {}".format(contador_edad))
    print("contador_sexo: {}".format(contador_genero))
    print("contador_ciudad: {}".format(contador_procedencia))
    sleep(PAUSA)

    # Nos fijamos si ya se concluyeron las tres busquedas
    busqueda_completa = \
        busqueda_por_edad_completa and \
        busqueda_por_genero_completa and \
        busqueda_por_procedencia_completa