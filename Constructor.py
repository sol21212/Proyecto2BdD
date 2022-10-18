class Constructor:

    def __init__(self):
        pass

    def menuInicial(self):
        print("POR FAVOR INDIQUE QUE PROCESO DESEA REALIZAR:")
        print("1. Iniciar sesión.")
        print("2. Cuenta nueva.")

        x = int(input(""))

        if x == 1:
            self.inicioSesion()
        if x == 2:
            self.crearCuenta()
        else:
            print("Error. Intente de nuevo.")
            self.menuInicial()

        return None

    def menuNormal(self):
        valor_salida = False
        while not valor_salida:
            print("Bienvenido al menu de IHealth")
            print("Por favor ingrese el numero de la opción que desea tomar:")
            print("1. Agregar nueva sesión.")
            print("2. Ver registro sesiones.")
            print("3. Cambiar tipo de plan.")
            print("4. Consulta estadísticas de una sesión.")
            print("5. Registrar peso semanal.")
            print("6. Consulta peso histórico.")
            print("7. Desactivar cuenta.")
            print("8. Salir.")


        return None

    def menuAdmin(self):
        pass

    def crearCuenta(self):
        pass

    def inicioSesion(self):
        pass
