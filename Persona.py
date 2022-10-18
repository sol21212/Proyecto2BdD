class Persona:

    def __init__(self, nombre, edad, altura, calorieIntake, pesoInicial, pesoActual, plan, contrasena, pago):
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

        self.registroPeso = [ pesoInicial]
        self.registroSesiones = []

    def getNombre(self):
        return self.nombre

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
        self.registro.append(pesoNuevo)
        return None

    def agregarSesion(self, sesionNueva):
        self.registroSesiones.append(sesionNueva)
        return None

    def finalizarSuscripcion(self):
        self.pago = None
        self.plan = None
        self.acceso = False
        return None

    def mostrarRegistroPeso(self):
        for i  in self.registroPeso:
            print("Registro No. "+ i + "| El peso fue de: " + self.registroPeso[i])

        return None

    # def mostrarRegistroSesiones(self):
    #     for i in self.registroSesiones:
    #         print("Sesion No. " + i + "| Datos de la sesion: " + self.registroSesiones[i])
    #
    #     return None