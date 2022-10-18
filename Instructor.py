class Instructor:

    def __init__(self, id, nombre, contrato, estadoCuenta, pago):
        self.ID = id
        self.nombre = nombre
        self.contrato = contrato
        self.estadoCuenta = estadoCuenta
        self.metodoPago = pago

    def getID(self):
        return self.ID

    def getNombre(self):
        return self.nombre

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
        return None

    def getContrato(self):
        return self.contrato

    def setContrato(self, nuevoContrato):
        self.contrato = nuevoContrato
        return None

    def getEstadoCuenta(self):
        return self.estadoCuenta

    def setEstadoCuenta(self, nuevoEstado):
        self.estadoCuenta = nuevoEstado
        return None

    def getMetodoPago(self):
        return self.metodoPago

    def cambioMetodoPago(self, nuevoMetodo):
        self.metodoPago = nuevoMetodo
        return None

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Contrato: ", self.contrato)
        print("Estado Cuenta: ", self.estadoCuenta)
        print("Método Pago: ", self.metodoPago)
        print("ID: ", self.ID)
