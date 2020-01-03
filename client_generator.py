#Generar aleatoriamente datos simulados de 1000 clientes, de ambos sexos,
#en un rango de edad desde los 18 hasta los 65 años, generando también
#su DNI y derivando su correo de su nombre.
from random import randint, choice, sample
import datetime
from faker import Faker
import string
import uuid
import io 

NRO_CLIENTES = 10
EDAD_MIN = 18 
EDAD_MAX = 65 


SEXO = ["M","F"]
DOMINIO_EMAIL = ["gmail.com",'yahoo.com',"hotmail.com"]

lista_clientes = []
nro = 0
lista_dni = []
lista_emails = []
nombres = ""
cadena_texto = "dni,nombres,apepat,apemat,genero,fechanac,correo,uuid \n"

def gen_dni():
    dni = randint(0,99999999)
    return dni 

def gen_sexo(genero,nombres):
    sexo = choice(SEXO)
    if sexo == "M":
        genero = "MASCULINO"
        NOMBRES = tuple(
           open('nombres_hombres.txt').read().splitlines()
        )
    else:
        genero = "FEMENINO"
        NOMBRES = tuple(
            open('nombres_mujeres.txt').read().splitlines()
        )
    return genero,nombres


#def gen_nombre():


'''
while len(lista_clientes) < NRO_CLIENTES: 



    # generamos nombre
    cantidad_nombres = randint(1,3)
    nombres = " ".join(sample(NOMBRES,cantidad_nombres))
    nombres = nombres.upper()
    APELLIDOS = tuple(
        open('apellidos.txt').read().splitlines()
    )
    apellido_paterno = choice(APELLIDOS).upper()
    apellido_materno = choice(APELLIDOS).upper()
    
    # generamos edad
    hoy = datetime.datetime.now()
     
    fake = Faker()
    start_date = datetime.date(year=hoy.year - 65, month=1, day=1)
    end_date = datetime.date(year=hoy.year - 18, month=hoy.month, day=hoy.day)
    fecha_nacimiento = fake.date_between(start_date=start_date, end_date=end_date)


    # generamos correo 
    opciones = randint(1,3)
    dominio = choice(DOMINIO_EMAIL)
    if opciones == 1:
        #una parte del nombre + número aleatorio
        nombre_parcial = randint(1,len(nombres))
        cadena = nombres[0:nombre_parcial].lower()
        cadena = cadena.replace(" ","") + str(randint(1,999))
    elif opciones == 2:
        nombre_parcial = nombres.lower()
        cadena = nombre_parcial + str(randint(1,99))
        cadena = cadena.replace(" ","")
    else:
        nombre_parcial = nombres[0] + apellido_paterno[0] + apellido_materno[0]
        cadena = nombre_parcial.lower() + str(fecha_nacimiento.year)
        
    email = cadena + "@" + dominio

    uuidcod = uuid.uuid4()

    if dni not in lista_dni and email not in lista_emails:
        nro += 1 
        lista_clientes.append(nro)

        print(f"CLIENTE Nro: {nro}")
        print(f"DNI: {dni:08d}")
        print(f"NOMBRES: {nombres} ")
        print(f"APELLIDO PATERNO: {apellido_paterno}")
        print(f"APELLIDO MATERNO: {apellido_materno}")
        print(f"GÉNERO: {genero}")
        print(f"FECHA DE NACIMIENTO: {fecha_nacimiento}")
        print(f"CORREO: {email}")
        print(f"UUID: {uuidcod}")
        print("="*60)

        cadena_texto += str(dni) + "," + nombres + "," + apellido_paterno + "," + apellido_materno + "," + genero + "," + str(fecha_nacimiento) + "," + email + "," + str(uuidcod) + "\n"



#print(cadena_texto)



with io.open('clientes.csv','w',encoding='utf8') as f:
    f.write(cadena_texto)
'''

if __name__ == "__main__": 
    # generamos DNI 
    print(gen_dni())
    # generamos sexo 
    print(gen_sexo())
    