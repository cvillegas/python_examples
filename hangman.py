from string import ascii_uppercase
from random import choice

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

ALFABETO = ascii_uppercase + 'Ñ'
CARACTER_DE_REEMPLAZO = '_'

MAX_INTENTOS_FALLIDOS = len(HANGMANPICS) - 1

FRASES = tuple(
    open('frases.txt').read().splitlines()
)

frase = choice(FRASES)

primera_vez = True
aciertos = []
errores = []
letra = None

while True:

    if not primera_vez:
        # Bucle infinito para leer una letra según las reglas
        while True:

            letra = input("Ingrese una letra: ").strip()

            if len(letra) > 1:
                print("ERROR: Debe ingresar únicamente una letra")
                continue

            if len(letra) == 0:
                print("ERROR: Debe ingresar una letra obligatoriamente")
                continue

            if letra not in ALFABETO:
                print("ERROR: El caracter ingresado no es válido")
                continue

            break

        # Detectar si es acierto ó error
        if letra is not None:
            if letra in frase:
                aciertos.append(letra)
            else:
                errores.append(letra)
            
    if primera_vez:
        print("*********************")
        print("*                   *")
        print("*  A H O R C A D O  *")
        print("*                   *") 
        print("*********************")

    frase_a_imprimir = []
    for c in frase:
        if (c in aciertos) or (c == ' '):
            frase_a_imprimir.append(c)
        else:
            frase_a_imprimir.append(CARACTER_DE_REEMPLAZO)
    print("Frase: {frase}".format(frase=' '.join(frase_a_imprimir)))
    if not primera_vez:
        print(f"Letra: {letra}")
    print("Errores: {errores}".format(errores=(' '.join(errores) if errores else 'Ninguno')))

    print(HANGMANPICS[len(errores)])

    if primera_vez:
        primera_vez = False

    # Verificamos si se ganó
    if CARACTER_DE_REEMPLAZO not in frase_a_imprimir:
        print("¡FELICITACIONES! ¡UD. HA ADIVINADO LA FRASE!")
        print(
            "¡El HOMBRE ESTUVO A SOLO {n} INTENTO(S) FALLIDOS MÁS DE SER AHORCADO!".format(
               n=MAX_INTENTOS_FALLIDOS - len(errores)
            )
        )
        break
    
    # Verificamos si perdió
    if  len(errores) == MAX_INTENTOS_FALLIDOS:
        print("¡LO SENTIMOS! ¡ALCANZÓ LOS 8 INTENTOS FALLIDOS MÁXIMOS PERMITIDOS!")
        print()
        print("!EL HOMBRE HA SIDO AHORCADO!")
        print()
        print("LA FRASE ERA:\n")
        print(frase)
        break



        

