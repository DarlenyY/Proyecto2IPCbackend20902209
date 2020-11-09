class solicitud:

    def __init__ (self,nombre,artista,album,fecha,imagen,spotify,youtube):
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.fecha = fecha
        self.imagen = imagen
        self.spotify = spotify
        self.youtube = youtube

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