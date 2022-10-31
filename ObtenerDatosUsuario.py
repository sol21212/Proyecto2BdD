import psycopg2
from Persona import *
from Sesion import *
from Instructor import *

from psycopg2 import Error
class ObtenerDatosUsuario():
    def __init__(self):
        self.conexion = psycopg2.connect(host='localhost', database='proyecto2', user='postgres', password='123456', )
        self.obtener = self.conexion.cursor()

    def jalar_usuarios(self, usuarios):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()

            print("Datos obtenidos de usuario")
            self.obtener.execute("SELECT * FROM usuario")
            personas = self.obtener.fetchall()
            for row in personas:
                nombre = str(row[0])
                edad = str(row[1])
                direccion = str(row[2])
                id_obtenido = str(row[3])
                altura = str(row[4])
                peso_actual = str(row[5])
                caloria_diarias = str(row[6])
                administrador = str(row[7])
                suscripcion_activa = str(row[8])
                estado_cuenta = str(row[9])
                pago = str(row[10])
                plan = str(row[11])

                usuario = Persona(nombre, edad, altura, caloria_diarias, peso_actual, peso_actual, plan, "123456",
                                    pago,
                                    id_obtenido)
                usuario.setAdminStatus(administrador)
                usuario.setAcceso(suscripcion_activa)
                usuario.setDireccion(direccion)
                usuarios.append(usuario)

                return usuarios

        except Exception as e:
            print(e)

        finally:
            print("Conexion desconectada.")
            self.obtener.close()

    def agregarUsuario(self, p):
        try:

            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            valor = """INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
                    VALUES({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})""".format(p.getNombre(), p.getEdad(), p.getDireccion(), p.getID(), p.getAltura(), p.pesoActual(), p.getCalorieIntake(), p.getAdminStatus(), p.getAdminStatus(), p.getAcceso(), p.getMetodoPago(), p.getPlan())

            print("Datos agregados a usuario")
            self.obtener.execute(valor)

        except Exception as e:
            print(e)

        finally:
            print("Conexion desconectada.")
            self.obtener.close()

    def jalar_sesiones(self, sesiones):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()

            print("Datos obtenidos de sesiones")
            self.obtener.execute("SELECT * FROM sesion")
            sesions = self.obtener.fetchall()
            for row in sesions:
                categoria = str(row[0])
                duracion = str(row[1])
                instructor=  str(row[2])
                fecha  = str(row[3])
                hora = str(row[4])
                id_sesion = str(row[5])

                sesion = Sesion(fecha, hora, duracion, instructor, categoria, id_sesion)
                sesiones.append(sesion)

                return sesiones

        except Exception as e:
            print(e)

        finally:
            print("Conexion desconectada.")
            self.obtener.close()

    def agregarSesion(self, s):
        try:
            s = Sesion()
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            valor = """INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
                    VALUES({}, {}, {}, {}, {}, {})""".format(s.getCategoria(), s.getDuracion(), s.getInstructor(), s.getFecha(), s.getHora(), s.getId_sesion())

            print("Datos agregados a sesion")
            self.obtener.execute(valor)

        except Exception as e:
            print(e)

        finally:
            print("Conexion desconectada.")
            self.obtener.close()