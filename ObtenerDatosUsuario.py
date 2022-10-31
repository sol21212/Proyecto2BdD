import psycopg2
from Persona import *
from datetime import date
from Sesion import *
from Instructor import *

from psycopg2 import Error
class ObtenerDatosUsuario():
    def __init__(self):
        self.conexion = psycopg2.connect(host='localhost', database='proyecto2', user='postgres', password='123456', )
        self.obtener = self.conexion.cursor()
        self.fecha = date.today()

    def jalar_usuarios(self, usuarios):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()


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
                usuario.registroPeso = self.jalar_registroPeso(usuario.registroPeso, id_obtenido)
                usuario.iwatchSesiones = self.jalar_iwatchsesiones(usuario.iwatchSesiones, id_obtenido)
                usuarios.append(usuario)

            print("Datos obtenidos de usuario")
            return usuarios


        except Exception as e:
            print(e)




    def agregarUsuario(self, p):
        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            valor = """INSERT INTO usuario(nombre, edad, direccion, id_usuario, altura, peso_actual, calorias_diarias, administrador, suscripcion_activa, estado_cuenta, pago, plan)
                    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(p.getNombre(), p.getEdad(), p.getDireccion(), p.getID(), p.getAltura(), p.getPesoActual(), p.getCalorieIntake(), p.getAdminStatus(), "Activo", p.getAcceso(), p.getMetodoPago(), p.getPlan())

            self.obtener.execute(valor)
            self.conexion.commit()

        except Exception as e:
            print(e)



    def jalar_sesiones(self, sesiones):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()


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

            print("Datos obtenidos de sesiones")
            return sesiones


        except Exception as e:
            print(e)


    def agregarSesion(self, s):
        try:

            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            valor = """INSERT INTO sesion(categoria, duracion, instructor, fecha, hora, id_sesion)
                    VALUES('{}', '{}', '{}', '{}', '{}', '{}')""".format(s.getCategoria(), s.getDuracion(), s.getInstructor(), s.getFecha(), s.getHora(), s.getId_sesion())

            print("Datos agregados a sesion")
            self.obtener.execute(valor)
            self.conexion.commit()

        except Exception as e:
            print(e)


    def jalar_instructores(self, instructores):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()


            self.obtener.execute("SELECT * FROM entrenador")
            entrenadores = self.obtener.fetchall()
            for row in entrenadores:
                id_entrenador =  str(row[0])
                contrato_horas =  str(row[1])
                metodo_pago =  str(row[2])

                instructor = Instructor(id_entrenador, "Nombre", contrato_horas, "0", metodo_pago)
                instructores.append(instructor)

            print("Datos obtenidos de instructores")
            return instructores


        except Exception as e:

            print(e)

    def agregarInstructor(self, s):
        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            valor = """INSERT INTO entrenador(id_entrenador, contrato_horas, metodo_pago)
                    VALUES({}, {}, '{}')""".format(s.getID(), s.getContrato(), s.getMetodoPago())

            print("Datos agregados a instructores")
            self.obtener.execute(valor)
            self.conexion.commit()

        except Exception as e:
            print(e)


    def jalar_registroPeso(self, registroSesiones, idUsuario):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()


            self.obtener.execute("SELECT * FROM registro_peso")
            registros = self.obtener.fetchall()
            for row in registros:
                fecha =  str(row[0])
                peso =  str(row[1])
                id_usuario =  str(row[2])

                if id_usuario == idUsuario:
                    registroSesiones.append(peso)

            print("Datos obtenidos de registroPeso")
            return registroSesiones

        except Exception as e:
            print(e)


    def agregarRegistroPeso(self, peso, idUsuario):
        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            fechass = str(self.fecha)
            valor = """INSERT INTO registro_peso(fecha, peso, id_usuario)
                    VALUES('{}', {}, {})""".format(fechass, peso, idUsuario)
            self.obtener.execute(valor)
            self.conexion.commit()
            print("Datos agregados a registro Peso")

        except Exception as e:
            print(e)


    def jalar_iwatchsesiones(self, sesiones, idUsuario):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()

            self.obtener.execute("SELECT * FROM iwatch_sesiones2")
            registros = self.obtener.fetchall()
            for row in registros:
                id_usuario =  str(row[0])
                id_sesion =  str(row[1])
                fecha =  str(row[2])
                hora = str(row[3])
                ritmo_cardiaco = str(row[4])
                calorias = str(row[5])
                tipo_ejercicio = str(row[6])

                if id_usuario == idUsuario:
                    sesion = Sesion_watch(id_sesion, id_usuario, ritmo_cardiaco, tipo_ejercicio, calorias, hora, fecha)
                    sesiones.append(sesion)
            print("Datos obtenidos de iWatch Sesiones")
            return sesiones

        except Exception as e:

            print(e)

    def agregariWatch(self, r):

        try:
            # print("Ingresar ID del usuario de interés:\n")
            # id_ingresado = input()
            valor = """INSERT INTO iwatch_sesiones2(id_usuario, id_sesion, fecha, hora, ritmo_cardiaco, calorias, tipo_ejercicio)
                    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(r.getIdUsuario(), r.getId_sesion(), r.getFecha(), r.getHora(), r.getRc(), r.getCalBurned(), r.getTipo_ejercicio())

            print("Datos agregados a iWatch Sesiones")
            self.obtener.execute(valor)
            self.conexion.commit()

        except Exception as e:
            print(e)
