from Sesion import *
class Persona:

    def __init__(self, nombre, edad, altura, calorieIntake, pesoInicial, pesoActual, plan, contrasena, pago, id):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.calorieIntake = calorieIntake
        self.pesoInicial = pesoInicial
        self.pesoActual = pesoActual
        self.plan = plan
        self.contrasena = contrasena
        self.pago = pago
        self.acceso = True
        self.admin = False
        sesion_zero = Sesion("", "", "", "", "", 0)
        self.registroPeso = [ pesoInicial]
        self.registroSesiones = [sesion_zero]
        self.id = id
        self.direccion = ""

    def getNombre(self):
        return self.nombre

    def getID(self):
        return self.id
    def setID(self, nuevoId):
        self.id = nuevoId
        return None

    def getAcceso(self):
        return self.acceso
    def setAcceso(self, nuevoA):
        self.acceso = nuevoA
        return None

    def getAdminStatus(self):
        return self.admin

    def setAdminStatus(self, newAdmin):
        self.admin = newAdmin
        return None

    def getAcceso(self):
        return self.acceso

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return None

    def getEdad(self):
        return self.edad

    def setEdad(self, nuevaEdad):
        self.edad = nuevaEdad
        return None

    def getAltura(self):
        return self.altura

    def setAltura(self, nuevaAltura):
        self.altura = nuevaAltura
        return None

    def getCalorieIntake(self):
        return self.calorieIntake

    def setCalorieIntake(self, nuevoCalorie):
        self.calorieIntake = nuevoCalorie
        return None

    def getPesoIncial(self):
        return self.pesoInicial

    def getPesoActual(self):
        return self.pesoActual

    def setPesoActual(self, nuevoPeso):
        self.pesoActual = nuevoPeso
        return None

    def getPlan(self):
        return self.plan

    def setPlan(self, nuevoPlan):
        self.plan = nuevoPlan
        return None

    def getContrasena(self):
        return self.contrasena

    def setContrasena(self, nuevaContrasena):
        self.contrasena = nuevaContrasena
        return None

    def getMetodoPago(self):
        return self.pago

    def setMetodoPago(self, nuevoMetodo):
        self.pago = nuevoMetodo
        return None

    def agregarPesoSemanal(self, pesoNuevo):
        self.pesoActual = pesoNuevo
        self.registroPeso.append(pesoNuevo)
        return None

    def agregarSesion(self, sesionNueva):
        self.registroSesiones.append(sesionNueva)
        return None

    def finalizarSuscripcion(self):
        self.pago = None
        self.plan = None
        self.acceso = False
        return None

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, nuevaDireccion):
        self.direccion = nuevaDireccion
        return None

    def mostrarRegistroPeso(self):
        for i  in range(len(self.registroPeso)):
            print("Registro No. ",i ,"| El peso fue de: " + self.registroPeso[i])

        return None
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Altura: ",self.altura)
        print("Calorías: ",self.calorieIntake)
        print("Peso Inicial: ",self.pesoInicial)
        print("Peso Actual: ",self.pesoActual)
        print("Plan: ",self.plan)
        print("Contraseña: ",self.contrasena)
        print("Pago: ",self.pago)
        print("Acceso: ",self.acceso)
        print("Admin: ",self.admin)
        print("ID: ",self.id)

    def mostrarRegistroSesiones(self):
        for i in range(len(self.registroSesiones)):
            sesionActual = self.registroSesiones[i]
            fecha = sesionActual.getFecha()
            hora = sesionActual.getHora()
            duracion = sesionActual.getDuracion()
            instructor = sesionActual.getInstructor()
            categoria = sesionActual.getCategoria()
            ID = sesionActual.getId_sesion()

            print("| Fecha: ", fecha ,
                                      "| Hora: " , hora ,
                                      "| Duracion: " , duracion ,
                                      "| Instructor: " , instructor ,
                                      "| Categoria: " , categoria ,
                                      "| ID: " , ID
                  )

        return None