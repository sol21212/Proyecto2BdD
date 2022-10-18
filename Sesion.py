class Sesion:
    
    def __init__(self, fecha, hora, duracion, instructor, categoria, id_sesion):
        self.fecha = fecha
        self.hora = hora
        self.duracion = duracion
        self.instructor = instructor
        self.categoria = categoria
        self.id_sesion = id_sesion
        
#----------------------------------------------------------------------------------

    def getFecha(self):
        return self.fecha
    
    def setFecha(self, nuevaFecha):
        self.fecha = nuevaFecha
        return None
    
#----------------------------------------------------------------------------------
    
    def getHora(self):
        return self.hora
    
    def setHora(self, nuevaHora):
        self.hora = nuevaHora
        return None
    
#----------------------------------------------------------------------------------
    
    def getDuracion(self):
        return self.duracion
    
    def setDuracion(self, nuevaDuracion):
        self.duracion = nuevaDuracion
        return None
    
#----------------------------------------------------------------------------------
    
    def getInstructor(self):
        return self.instructor
    
    def setInstructor(self, nuevoInstructor):
        self.instructor = nuevoInstructor
        return None
        
#----------------------------------------------------------------------------------
    
    def getCategoria(self):
        return self.categoria
    
    def setCategoria(self, nuevaCategoria):
        self.categoria = nuevaCategoria
        return None

#----------------------------------------------------------------------------------
    
    def getId_sesion(self):
        return self.id_sesion
    
    def setId_sesion(self, nuevoId_sesion):
        self.id_sesion = nuevoId_sesion
        return None

    def mostrarDatos(self):
        print("| Fecha: " , self.fecha ,
              "| Hora: " , self.hora ,
              "| Duracion: " , self.duracion ,
              "| Instructor: " , self.instructor ,
              "| Categoria: " , self.categoria ,
              "| ID: " , self.id_sesion
              )
        return None