from Persona import *
from Sesion import *
from Instructor import *


class Constructor:

    def __init__(self):
        self.entrenador_zero = Instructor(0, "Nombre", "contrato", "estadoCuenta", "metodoPago")
        self.sesion_zero = Sesion("", "", "", "", "", 0)
        self.usuario_zero = Persona("", "", "", "", "", "", "", contrasena="1",pago="", id=1)
        self.usuario_uno = Persona("", "", "", "", "", "", "", contrasena="123", pago="", id=123)
        self.usuario_zero.setAdminStatus(True)
        self.sesiones = [self.sesion_zero]
        self.usuarios = [self.usuario_zero, self.usuario_uno]
        self.instructores = [self.sesion_zero]

    def menuInicial(self):
        valor_salida = False
        while not valor_salida:
            print("POR FAVOR INDIQUE QUE PROCESO DESEA REALIZAR:")
            print("1. Iniciar sesión.")
            print("2. Cuenta nueva.")

            x = int(input(""))

            if x == 1:
                self.inicioSesion()
                valor_salida = True
            elif x == 2:
                self.crearCuenta()
                valor_salida = True
            else:
                print("Error. Intente de nuevo.")

        return None

    def menuNormal(self, persona):
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

            x = int(input(""))

            if x == 1:
                fecha = input("Ingrese la fecha de la sesión:  ")
                hora = input("Ingrese la hora de la sesión:  ")
                duracion = input("Ingrese la duración de la sesión:  ")
                instructor = input("Ingrese el ID del Instructor:  ")
                categoria = input("Ingrese la categoria de la sesión:  ")
                ultimaSesion = self.sesiones[len(self.sesiones) - 1]
                nuevoID = ultimaSesion.id_sesion + 1

                sesion = Sesion(fecha, hora, duracion, instructor, categoria, nuevoID)
                persona.agregarSesion(sesion)
                self.sesiones.append(sesion)
            elif x == 2:
                persona.mostrarRegistroSesiones()
            elif x == 3:
                tipoPlan = persona.getPlan()
                print("Su tipo de plan Actual es " + tipoPlan)
                print("Escoja por favor el plan que quiera: ")
                print("1. Plan ORO (Q250.00).")
                print("2. Plan DIAMANTE (Q500.00).")
                eleccion = int(input(""))
                if eleccion == 1:
                    persona.setPlan("Plan Oro")
                elif eleccion == 2:
                    persona.setPlan("Plan Diamante")
                else:
                    print("Error. Intente de nuevo.")
            elif x == 4:
                sesion = self.sesion_zero
                idSesionBuscar = input("Ingrese el ID de la Sesion que desea ver: .")
                for l in range(len(self.sesiones)):
                    if idSesionBuscar == self.sesiones[l].getId_sesion:
                        sesion = self.sesiones[l]

                sesion.mostrarDatos()

            elif x == 5:
                peso = input("Ingrese su peso Actual:  ")
                persona.setPesoActual(peso)
                persona.agregarPesoSemanal(peso)

            elif x == 6:
                persona.mostrarRegistroPeso()
            elif x == 7:
                persona.finalizarSuscripcion()
                valor_salida = True
            elif x == 8:
                valor_salida = True
            else:
                print("Error. Intente de nuevo.")

        return None

    def menuAdmin(self, persona):
        valor_salida = False
        while not valor_salida:
            print("Bienvenido al menu ADMIN de IHealth")
            print("Por favor ingrese el numero de la opción que desea tomar:")
            print("0. Crear Usuario.")
            print("1. Agregar Instructor.")
            print("2. Modificar Instructor.")
            print("3. Dar de baja instructor.")
            print("4. Agregar sesion.")
            print("5. Modificar sesion.")
            print("6. Dar de baja sesion.")
            print("7. Modificar usuarios.")
            print("8. Dar de baja usuario.")
            print("9. Modulo de Reportes.")
            print("10. Salir.")

            x = int(input(""))

            if x == 0:
                #Crear Usuario
                nombre = input("Ingrese el nombre del usuario:  ")
                edad = input("Ingrese la edad del usuario:  ")
                altura = input("Ingrese la altura del usuario:  ")
                calorieIntake = input("Ingrese el calorie Intake del usuario:  ")
                pesoIncial = input("Ingrese el peso inicial del usuario:  ")
                pesoActual = pesoIncial
                contrasena = input("Ingrese la contrasena del usuario:  ")
                plan = input("Ingrese el plan del usuario:  ")
                metodoPago = input("Ingrese el metodo de pago del usuario:  ")
                ultimoUsuario = self.usuarios[len(self.usuarios) - 1]
                nuevoID = ultimoUsuario.id + 1

                usuario = Persona(nombre, edad, altura, calorieIntake, pesoIncial, pesoActual, plan, contrasena,
                                  metodoPago, nuevoID)
                self.usuarios.append(usuario)

                self.imprimirUsuarios()

            elif x == 1:
                #Agregar Instructor
                nombre = input("Ingrese el nombre del instructor:  ")
                contrato = input("Ingrese el contrato del instructor:  ")
                estadoCuenta = input("Ingrese el estado de Cuenta del instructor:  ")
                metodoPago = input("Ingrese el metodo de pago del instructor:  ")
                nuevoID = len(self.instructores)

                instructor = Instructor(nuevoID, nombre, contrato, estadoCuenta, metodoPago)
                self.instructores.append(instructor)

                self.imprimirInstructores()
            elif x == 2:
                # Modificar Instructor
                instructor = self.entrenador_zero
                valor = 0
                idInstructor = input("Por favor ingrese el ID Instructor que desea modificar:")
                for l in range(len(self.instructores)):
                    instructor = self.instructores[l]
                    if l == idInstructor:
                        instructor = self.instructores[l]
                        instructor.imprimir()
                        self.instructores.pop(l)
                        valor = l

                print("Por favor ingrese el numero del aspecto que desea modificar:")
                print("1. Nombre.")
                print("2. Contrato.")
                print("3. Estado Cuenta.")
                print("4. Metodo de Pago.")

                eleccion = int(input(""))
                nuevoDato = input("Ingrese el nuevo dato a reemplazarlo: ")
                if eleccion == 1:
                    instructor.setNombre(nuevoDato)
                elif eleccion == 2:
                    instructor.setContrato(nuevoDato)
                elif eleccion == 3:
                    instructor.setEstadoCuenta(nuevoDato)
                elif eleccion == 4:
                    instructor.cambioMetodoPago(nuevoDato)

                self.instructores.insert(valor, instructor)
                self.imprimirInstructores()

            elif x == 3:
                #Dar de baja instructor
                instructor = self.entrenador_zero
                idInstructor = input("Por favor ingrese el ID Instructor que desea dar de baja:")
                for l in range(len(self.instructores)):
                    if l == idInstructor:
                        instructor = self.instructores[l]
                        self.instructores.pop(l)
                self.imprimirInstructores()

            elif x == 4:
                #Agregar Sesion
                fecha = input("Ingrese la fecha de la sesión:  ")
                hora = input("Ingrese la hora de la sesión:  ")
                duracion = input("Ingrese la duración de la sesión:  ")
                instructor = input("Ingrese el ID del Instructor:  ")
                categoria = input("Ingrese la categoria de la sesión:  ")
                ultimaSesion = self.sesiones[len(self.sesiones) - 1]
                nuevoID = ultimaSesion.id_sesion + 1

                sesion = Sesion(fecha, hora, duracion, instructor, categoria, nuevoID)
                self.sesiones.append(sesion)
                self.imprimirSesiones()

            elif x == 5:
                # Modificar Sesion
                sesion = self.sesion_zero
                idSesion = input("Por favor ingrese el ID de la Sesion que desea modificar:")
                valor = 0
                for l in range(len(self.sesiones)):
                    if self.sesiones[l].getId_sesion() == idSesion:
                        sesion = self.sesiones[l]
                        self.sesiones.pop(l)
                        valor = l


                print("Por favor ingrese el numero del aspecto que desea modificar:")
                print("1. Fecha.")
                print("2. Hora.")
                print("3. Duracion.")
                print("4. Instructor.")
                print("5. Categoria.")

                eleccion = int(input(""))
                nuevoDato = input("Ingrese el nuevo dato a reemplazarlo: ")
                if eleccion == 1:
                    sesion.setFecha(nuevoDato)
                elif eleccion == 2:
                    sesion.setHora(nuevoDato)
                elif eleccion == 3:
                    sesion.setDuracion(nuevoDato)
                elif eleccion == 4:
                    sesion.setInstructor(nuevoDato)
                elif eleccion == 5:
                    sesion.setCategoria(nuevoDato)

                self.sesiones.insert(valor, sesion)
                self.imprimirSesiones()

            elif x == 6:
                #Dar de baja sesion
                sesion = self.sesion_zero
                idSesion = input("Por favor ingrese el ID de la Sesion que desea modificar:")
                for l in range(len(self.sesiones)):
                    if self.sesiones[l].getId_sesion() == idSesion:
                        sesion = self.sesiones[l]
                        self.sesiones.pop(l)

                self.imprimirSesiones()

            elif x == 7:
                # Modificar Usuario
                usuario = self.usuario_zero
                idUser = input("Por favor ingrese el ID del Usuario que desea modificar:")
                valor = 0
                for l in range(len(self.usuarios)):
                    if self.usuarios[l].getID() == idUser:
                        usuario = self.usuarios[l]
                        self.usuarios.pop(l)
                        valor = l


                print("Por favor ingrese el numero del aspecto que desea modificar:")
                print("1. Nombre.")
                print("2. Edad.")
                print("3. Altura.")
                print("4. Calorie Intake.")
                print("5. Contrasena.")
                print("6. Peso Actual.")
                print("7. Plan.")
                print("8. Pago.")
                print("9. Acceso.")
                print("10. Admin Status.")

                eleccion = int(input(""))
                nuevoDato = input("Ingrese el nuevo dato a reemplazarlo: ")
                if eleccion == 1:
                    usuario.setNombre(nuevoDato)
                elif eleccion == 2:
                    usuario.setEdad(nuevoDato)
                elif eleccion == 3:
                    usuario.setAltura(nuevoDato)
                elif eleccion == 4:
                    usuario.setCalorieIntake(nuevoDato)
                elif eleccion == 5:
                    usuario.setContrasena(nuevoDato)
                elif eleccion == 6:
                    usuario.setPesoActual(nuevoDato)
                elif eleccion == 7:
                    usuario.setPlan(nuevoDato)
                elif eleccion == 8:
                    usuario.setMetodoPago(nuevoDato)
                elif eleccion == 9:
                    usuario.setAcceso(nuevoDato)
                elif eleccion == 10:
                    usuario.setAdminStatus(nuevoDato)

                self.usuarios.insert(valor, usuario)
                self.imprimirUsuarios()


            elif x == 8:
                #Dar de baja usuario
                usuario = self.usuario_zero
                idUser = input("Por favor ingrese el ID del Usuario que desea dar de baja:")
                for l in range(len(self.usuarios)):
                    if self.usuarios[l].getID() == idUser:
                        usuario = self.usuarios[l]
                        usuario.finalizarSuscripcion()
                        usuario.imprimir()

            elif x == 9:
                # Modulo Estadisticas
                print("Top 10 Sesiones que más usuarios tuvieron.")
                print("Cantidad de sesiones y usuarios por cada categoría.")
                print("El top 5 de los entrenadores que los usuarios prefieren. ")
                print("La cantidad de cuentas diamante que se han creado en los últimos 6 meses. ")
                print("¿Cuál es la hora pico donde el servicio es más utilizado?")
            elif x == 10:
                valor_salida = True
            else:
                print("Error. Intente de nuevo.")

        return None

    def crearCuenta(self):

        nombre = input("Ingrese su nombre:  ")
        edad = input("Ingrese su edad:  ")
        altura = input("Ingrese su altura:  ")
        calorieIntake = input("Ingrese sus calorias diarias:  ")
        pesoIncial = input("Ingrese su peso inicial :  ")
        pesoActual = pesoIncial
        contrasena = input("Ingrese su contrasena:  ")
        plan = input("Ingrese su plan del usuario (ORO/DIAMANTE):  ")
        metodoPago = input("Ingrese el metodo de pago:  ")

        nuevoID = len(self.usuarios)

        usuario = Persona(nombre, edad, altura, calorieIntake, pesoIncial, pesoActual, plan, contrasena, metodoPago,
                          nuevoID)
        if plan == "ADMIN":
            usuario.admin = True
        self.usuarios.append(usuario)

        if usuario.admin == True:
            self.menuAdmin(usuario)
        else:
            self.menuNormal(usuario)

    def inicioSesion(self):
        entrada = False
        usuario = self.usuario_zero
        valor = 0
        while not entrada:
            idSearch = int(input("Ingrese el ID del usuario: "))
            passwordSearch = str(input("Ingrese la contraseña del usuario: "))
            usuario = self.usuario_zero
            for l in range(len(self.usuarios)):
                usuario = self.usuarios[l]
                if usuario.getID() == idSearch and usuario.getContrasena() == passwordSearch:
                    usuario = self.usuarios[l]

                    entrada = True


        if usuario.getAdminStatus() == True:
            self.menuAdmin(usuario)
        else:
            self.menuNormal(usuario)


    def imprimirSesiones(self):

        for i in self.sesiones:
            print("---------------------------------")
            i.imprimir()

    def imprimirUsuarios(self):

        for i in self.usuarios:
            print("---------------------------------")
            i.imprimir()

    def imprimirInstructores(self):
        for i in self.instructores:
            print("---------------------------------")
            i.imprimir()