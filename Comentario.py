class comentario:

    def __init__ (self,id,user,texto):
        self.id = id
        self.user = user
        self.texto = texto

    def getId(self):
        return self.id

    def getUser(self):
        return self.user

    def getTexto(self):
        return self.texto