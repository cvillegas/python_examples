#!/usr/bin/env python3
# tabla_de_multiplicar.py
"""
Imprimir las tablas de multiplicar desde
desde el 1 hasta el 12, considerando que debe
calcularse los valores del 1 al 12 en cada tabla.

Tabla del 1
===========

 1 x  1 =   1
 1 x  2 =   2
...
 1 x 12 =  12

...

Tabla del 12
=============

12 x  1 =  12
..
12 x 12 = 144
"""

TABLA_INICIAL = 10
TABLA_FINAL = 20

MULTIPLICANDO_INICIAL = 1
MULTIPLICANDO_FINAL = 12

for t in range(TABLA_INICIAL, TABLA_FINAL + 1):

    base = t

    titulo = f"Tabla del {base}"
    print(titulo)
    print("="*len(titulo) + "\n")

    for m in range(MULTIPLICANDO_INICIAL, MULTIPLICANDO_FINAL + 1):
        plantilla = "{multiplicando:2d} x {base:2d} = {multiplicacion:3d}"
        print(plantilla.format(multiplicando=m, base=base, multiplicacion=m*base))
    
    print()
