"""
Tirar un dado 100 veces y acumular los valores obtenidos para
imprimirlos al final del programa
"""

from random import randint

INICIO_RANGO_DADO = 1
FIN_RANGO_DADO = 6

VECES = 100

acumulador = 0 # que es el elemento neutro de la suma
for v in range(VECES):
    valor = randint(INICIO_RANGO_DADO, FIN_RANGO_DADO)
    acumulador += valor

print(f"Valor acumulado en {VECES} lanzamientos: {acumulador}")