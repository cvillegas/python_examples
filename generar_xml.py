"""
Escribir una función que genere un documento XML a partir
de la invocación a la misma, de la siguiente manera:

generar_xml(
    "empleado", 
    nombre="Juan Perez",
    "edad"=20,
    "sexo"="M",
    "codigo"="123456",
    "as_attributes"=True
)

La firma de la función es así:

def generar_xml(raiz, **kwargs)

Usar el método pop() para extraer la llave "as_attributes"
en caso que esté presente en el diccionario kwargs.

as_attributes = kwargs.pop('as_attributes', False)

Esto generaría el siguiente documento XML:

<?xml version="1.0"?>
<empleado nombre="Juan Perez" edad=20 sexo="M" codigo="123456" />

En cambio si as_attributes es False:

<?xml version="1.0"?>
<empleado>
    <nombre>Juan Perez</nombre>
    <edad>20</edad>
    <sexo>M</sexo>
    <codigo>123456</codigo> 
</empleado>
"""