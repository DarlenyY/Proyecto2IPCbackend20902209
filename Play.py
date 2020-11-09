class play:

    def __init__ (self,id,user,nombre,artista,album,fecha,imagen,spotify,youtube):
        self.id = id
        self.user= user
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.fecha = fecha
        self.imagen = imagen
        self.spotify = spotify
        self.youtube = youtube

    def getId(self):
        return self.id

    def getUser(self):
        return self.user

    def getNombre(self):
        return self.nombre

    def getArtista(self):
        return self.artista

    def getImagen(self):
        return self.imagen

    def getFecha(self):
        return self.fecha

    def getSpotify(self):
        return self.spotify

    def getYoutube(self):
        return self.youtube
    
    def getAlbum(self):
        return self.album

    def setId(self,id):
        self.id = id
    
    def setUser(self,user):
        self.user = user

    def setNombre(self,nombre):
        self.nombre = nombre

    def setArtista(self,artista):
        self.artista = artista
    
    def setImagen(self,imagen):
        self.imagen = imagen
    
    def setFecha(self,fecha):
        self.fecha = fecha

    def setAlbum(self,album):
        self.album = album

    def setSpotify(self,spotify):
        self.spotify = spotify
    
    def setYoutube(self,youtube):
        self.youtube = youtube