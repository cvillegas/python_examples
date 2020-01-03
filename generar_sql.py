"""
Escribir una función en Python que genere sentencias de SQL.

Ejemplo:

select("empleados", sexo="M", sueldo__gte=1500, jefe__isnull=False)

Esto debe generar la sentencia siguiente:

SELECT * FROM empleados WHERE sexo = 'M' AND sueldo >= 1500 AND jefe IS NOT NULL

La firma de la función debe ser:

def select(tabla, campos=[], **kwargs)

Cuando la lista de campos está vacía debe reemplazarse por "*"

Los sufijos en los nombres de los campos se expande de la siguiente manera:

__gt -> >
__gte -> >=
__lt -> <
__lte -> <=
__isnull = True -> IS NULL
__isnull = False -> IS NOT NULL
__different -> <>
__like -> LIKE 

Ademas, la función debe colocar comillas alrededor de los valores de tipo string
pero no debe colocarlas cuando se trate de enteros, flotantes y booleanos.
"""

MAPEO = {
    '__gt': '>',
    '__gte': '>=',
    '__lt': '<',
    '__lte': '<=',
    '__different': '<>',
    '__like': 'LIKE'
}


def select(tabla, campos=[], **kwargs):
    template = "SELECT {campos} FROM {tabla} {condiciones}"
    if campos:
        fcampos = ', '.join(campos)
    else:
        fcampos = '*'
    if kwargs:
        partes = []
        for k, v in kwargs.items():
            partes_segmento = []
            operador = '='
            nombre_campo = k
            for sufijo, reemplazo in MAPEO.items():
                if k.endswith(sufijo):
                    operador = reemplazo
                    nombre_campo = k[:-1*len(sufijo)]
                    break
            if k.endswith("__isnull"):
                if v == True:
                    operador = "IS NULL"
                elif v == False:
                    operador = 'IS NOT NULL'
                nombre_campo = k[:-1*len("__isnull")]
                partes_segmento.append(nombre_campo)
                partes_segmento.append(operador)
            else:
                partes_segmento.append(nombre_campo)
                partes_segmento.append(operador)
                if type(v) is str:
                    partes_segmento.append(f"\"{v}\"")
                else:
                    partes_segmento.append(str(v))
            segmento = ' '.join(partes_segmento)
            partes.append(segmento)
        condiciones = "WHERE " + ' AND '.join(partes)
    else:
        condiciones = ''
    return template.format(
        campos=fcampos,
        tabla=tabla,
        condiciones=condiciones
    ).strip()

if __name__ == '__main__':
    sql = select("empleados", ["cod_empleado", "apepat", "apemat"], sexo="M", sueldo__gte=1500, jefe__isnull=False)
    print(sql)