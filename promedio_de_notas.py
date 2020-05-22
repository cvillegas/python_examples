# Name: promedio_de_notas.py
# Version: 0.1
# Author: Cesar Villegas Ureta - https//www.slayerx.org/
# GitHub repo: https://github.com/cvillegas/python_examples
# License: MIT License
# Description: Sacar promedio de las notas ingresadas

"""
Escribir un programa que solicite el ingreso por teclado
de un valor flotante  entre 0.0 y 20.0 que corresponde a la
nota de una evaluación se irá acumulando en la variable
`acumulador`.

Al mismo tiempo, se deberá contar el número de notas que se van
ingresando en la variable `contador`.

Para dejar de ingresar más notas y obtener el promedio deberá
ingresarse el valor `-1`.

Corrida de ejemplo:

Ingrese una nota: 10.5
Ingrese una nota: Hola
ERROR: El valor no puede ser convertido a flotante
Ingrese una nota: 100
ERROR: El valor debe estar entre 0.0 y 20.0
Ingrese una nota: 19.5
Ingrese una nota: -1

Notas ingresadas: 2
Promedio de notas: 15.0
"""
from builtins import breakpoint

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 20.0

FINALIZADOR = -1

acumulador = 0.0
contador = 0

print("Para dejar de ingresar más notas y obtener el promedio deberá ingresarse el valor `-1` \n")

# Leer infinitas notas
while True: 
    # Lee una nota
    while True:
        try:
            valor = input("Ingrese una nota: ")
            valor = float(valor)
            if int(valor) == FINALIZADOR:
                break
            if (valor < NOTA_MINIMA) or (valor > NOTA_MAXIMA):
                print(
                    "ERROR: El valor debe estar {minimo:.1f} y {maximo:.1f}".format(
                        minimo=NOTA_MINIMA,
                        maximo=NOTA_MAXIMA
                    )
                )
            break
        except ValueError:
            print("ERROR: El valor no puede ser convertido a flotante")
    if int(valor) == FINALIZADOR:
        break
    contador += 1
    acumulador += valor

#promedio = 0.0
#if contador > 0:
#    promedio = acumulador / contador

try:
    promedio = acumulador / contador
except ZeroDivisionError:
    promedio = 0.0

print(f"\n Notas ingresadas: {contador}")
print(f"Promedio de notas: {promedio:.2f}")