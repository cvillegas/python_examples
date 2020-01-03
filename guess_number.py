"""
El programa genera un numero aleatorio entre 1 y 100
y le solicita al usuario que ingrese un numero entero
en el mismo rango.

Si ingresa un numero menor al numero por adivinar 
se le indica al usuario que el numero es mayor.

Si ingresa un numero mayor al numero por adivinar
se le indica al usuario que el número es menor.

Si adivina el numero se imprime el mensaje:

¡El número era X! ¡Ud. adivinó en N intentos!

En caso de que su supere el máximo de intentos:

¡Lo sentimos! Ud. ha superado el máximo de 10 intentos.

Luego de cada intento, el programa deberá indicar cuantos
intentos aún le quedan al usuario.
"""
# import the random library 
from random import randint

INICIO_RANGO = 1
FIN_RANGO = 100

por_adivinar = randint(INICIO_RANGO, FIN_RANGO)
numero = 0
intentos = 10

while numero != por_adivinar:

    # Read the number
    while True:
         numero = input(f"Ingrese un número entre {INICIO_RANGO} y {FIN_RANGO}: ")
         numero = numero.strip()
         try:
            numero = int(numero)
            if (numero < INICIO_RANGO) or (numero > FIN_RANGO):
                print("ERROR: El número está fuera de rango")
                continue
            break
         except ValueError:
            print("ERROR: El número debe ser un entero")

    # Compare
    if numero > por_adivinar:
        print(f"AYUDA: El número por adivinar es menor que {numero}")
    elif numero < por_adivinar:
        print(f"AYUDA: El número por adivinar es mayor que {numero}")
    
    intentos = intentos - 1 
    if intentos == 0: 
        break
    else:
        print(f"Le quedan {intentos} intentos")

if intentos == 0:
    print(f"¡El número era {por_adivinar}! ¡Ud. perdió!")
else: 
    print(f"¡El número era {por_adivinar}! ¡Ud. adivinó!")

