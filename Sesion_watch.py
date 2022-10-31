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

#----------------------------------------------------------------------------------
    
    def getFc(self):
        return self.fc
    
    def setFc(self, nuevaFc):
        self.fc = nuevaFc
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