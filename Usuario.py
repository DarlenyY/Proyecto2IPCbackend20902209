class usuario:

    def __init__ (self,nombre,apellido,user,contrasena,tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.user = user
        self.contrasena = contrasena
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getUser(self):
        return self.user

    def getContrasena(self):
        return self.contrasena

    def getTipo(self):
        return self.tipo

    def setTipo(self,tipo):
        self.tipo = tipo

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setUser(self,user):
        self.user = user

    def setContrasena(self,contrasena):
        self.contrasena = contrasena