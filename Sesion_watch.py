class Sesion_watch:
    
    def __init__(self, id_sesion, id_usuario, rc, tipo_ejercicio, calBurned, hora, fecha):
        self.id_sesion = id_sesion
        self.rc = rc
        self.id_usuario = id_usuario
        self.tipo_ejercicio = tipo_ejercicio
        self.calBurned = calBurned
        self.hora = hora
        self.fecha = fecha


#----------------------------------------------------------------------------------
        
    def getId_sesion(self):
        return self.id_sesion
    
    def setId_sesion(self, nuevoId_sesion):
        self.id_sesion = nuevoId_sesion
        return None

    def getIdSesion(self):
        return self.id_sesion

    def getIdUsuario(self):
        return self.id_usuario

    def getFecha(self):
        return self.fecha

    def getHora(self):
        return self.hora

#----------------------------------------------------------------------------------
    
    def getRc(self):
        return self.rc
    
    def setRc(self, nuevaRc):
        self.rc = nuevaRc
        return None
    
#----------------------------------------------------------------------------------
    
    def getTipo_ejercicio(self):
        return self.tipo_ejercicio
    
    def setTipo_ejericio(self, nuevoTipo_ejercicio):
        self.tipo_ejercicio = nuevoTipo_ejercicio
        return None

#----------------------------------------------------------------------------------
    
    def getCalBurned(self):
        return self.calBurned
    
    def setCalBurned(self, nuevasCalBurned):
        self.calBurned = nuevasCalBurned
        return None