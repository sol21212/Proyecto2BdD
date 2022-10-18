import psycopg2
from psycopg2 import Error

try:
    conexion = psycopg2.connect(database = "", user = "", password = "", host = "", port = "")
    obtener = conexion.cursor()
    print("Ingresar ID del usuario de interés:\n")
    id_ingresado = input()
    
    print("Datos obtenidos")
    obtener.execute(SELECT* FROM usuario WHERE id_usuario = id_ingresado)
    obtener.fetchall()
    for row in obtener:
        nombre = str(row[0])
        edad = str(row[1])
        direccion = str(row[2])
        id_obtenido = str(row[3])
        altura = str(row[4])
        peso_actual = str(row[5])
        caloria_diarias = str(row[6])
        administrador = str(row[7])
        suscripcion_activa = str(row[8])
        suscripcion_activa = str(row[9])
        pago = str(row[10])
        plan = str(row[11])
        
    print("Nombre del usuario: ", {nombre})
    print("edad: ", {edad})
    print("direccion residencial: ", {direccion})
    print("id del usuario: ", {id_obtenido})
    print("altura en metros: ", {altura})
    print("peso en libras: ", {peso_actual})
    print("calorias quemadas diariamente: ", {calorias_diarias})
    print("administrador: ", {administrador})
    print("cuenta con suscripcion activa: ", {suscripcion_activa})
    print("estado de cuenta: ", {estado_cuenta})
    print("pago: ", {pago})
    print("tipo de plan: ", {plan})

except:
    print("Error en la conexion, por favor probar de nuevo")
    