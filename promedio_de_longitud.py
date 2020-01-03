texto = input("Ingrese un texto: ")
texto = texto.strip()
segmentos = texto.split(' ')

acumulador = 0
contador = 0

for s in segmentos:
    longitud = len(s)
    acumulador += longitud
    contador += 1

try:
    longitud_promedio = acumulador / contador
except ZeroDivisionError:
    longitud_promedio = 0.0

plantilla  = "Longitud promedio de {contador} palabras encontrados "
plantilla += "en un texto de {longitud_texto} caracteres: {promedio:.2f}"
print(
    plantilla.format(
        contador=contador,
        longitud_texto=len(texto),
        promedio=longitud_promedio
    )
)