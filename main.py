from flask import Flask,jsonify,request
from  flask_cors import CORS
from  Usuario import usuario
from Solicitud import solicitud
from Cancion import cancion
from Play import play
from Comentario import comentario
import json
import re

app = Flask(__name__)
CORS(app) 
Solicitudes = []
Playlist = []
Comentarios = []
Canciones = []
contCancion = 0
Usuarios = []
Usuarios.append(usuario('Usuario','Maestro','admin','admin',2))
@app.route("/", methods = ["GET"])
def rutaInicial ():  
    return ('Principal')

#Mostrar todos los usuarios
@app.route('/Personas', methods= ['GET'])
def obtenerUsuarios():
    global Usuarios
    Datos = []
    for us in Usuarios:
        if us.getTipo()== 1:
             Dato = { 
            'nombre':us.getNombre(), 
            'apellido':us.getApellido(), 
            'user':us.getUser(),
            'contracena':us.getContrasena()
            }
             Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Mostrar Canciones
@app.route('/Canciones', methods= ['GET'])
def obtenerCanciones():
    global Canciones
    Datos = []
    for us in Canciones:
        Dato = { 
            'id':us.getId(),
            'nombre':us.getNombre(), 
            'artista':us.getArtista(), 
            'album':us.getAlbum(),
            'fecha':us.getFecha(),
            'imagen':us.getImagen(),
            'spotify':us.getSpotify(),
            'youtube':us.getYoutube()
         }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Buscar
@app.route('/Buscar/<string:palabra>', methods= ['GET'])
def obtenerbusqueda(palabra):
    global Canciones
    Datos = []
    Palabra = palabra.lower()
    for us in Canciones:
        cadena = us.getNombre().lower()
        if cadena.find(Palabra) >= 0:
            Dato = { 
            'id':us.getId(),
            'nombre':us.getNombre(), 
            'artista':us.getArtista(), 
            'album':us.getAlbum(),
            'fecha':us.getFecha(),
            'imagen':us.getImagen(),
            'spotify':us.getSpotify(),
            'youtube':us.getYoutube()
            }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Mostrar Detalles
@app.route('/PlayVer/<int:id>', methods= ['GET'])
def obtenerCancion(id):
    global Canciones
    for us in Canciones:
        if id == us.getId():
             Dato = { 
            'id':us.getId(),
            'nombre':us.getNombre(), 
            'artista':us.getArtista(), 
            'album':us.getAlbum(),
            'fecha':us.getFecha(),
            'imagen':us.getImagen(),
            'spotify':us.getSpotify(),
            'youtube':us.getYoutube()
            }
    respuesta = jsonify(Dato)
    return(respuesta)

#Mostrar Playlist
@app.route('/Play/<string:user>', methods= ['GET'])
def obtenerPlay(user):
    global Playlist
    Datos = []
    for us in Playlist:
        if user == us.getUser():
            Dato = { 
            'user':us.getUser(),
            'id':us.getId(),
            'nombre':us.getNombre(), 
            'artista':us.getArtista(), 
            'album':us.getAlbum(),
            'fecha':us.getFecha(),
            'imagen':us.getImagen(),
            'spotify':us.getSpotify(),
            'youtube':us.getYoutube()
            }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Mostrar Comentarios
@app.route('/Com', methods= ['GET'])
def obtenerComentarios():
    global Comentarios
    Datos = []
    for co in Comentarios:
       # if id == us.getId():
            Dato = { 
            'id':co.getId(),
            'user':co.getUser(),
            'texto':co.getTexto()
            }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Mostrar Solicitudes
@app.route('/Solicitudes', methods= ['GET'])
def obtenerSolicitudes():
    global Solicitudes
    Datos = []
    for Sol in Solicitudes:
        Dato = { 
            'nombre':Sol.getNombre(), 
            'artista':Sol.getArtista(),
            'album':Sol.getAlbum(),
            'fecha':Sol.getFecha(),
            'imagen':Sol.getImagen(),
            'spotify':Sol.getSpotify(),
            'youtube':Sol.getYoutube()
         }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

#Eliminar usuarios
@app.route('/Personas/<string:user>', methods=['DELETE'])
def EliminarPersona(user):
    global Usuarios
    for i in range(len(Usuarios)):
        if user == Usuarios[i].getUser():
            del Usuarios[i]
            break
    return jsonify({'message':'Se elimino el dato exitosamente'})


#Eliminar Canciones
@app.route('/Canciones/<int:id>', methods=['DELETE'])
def EliminarCancion(id):
    global Canciones, Playlist
    cont = len(Playlist)
    for i in range(len(Canciones)):
        if id == Canciones[i].getId():
            del Canciones[i]
            break
    for i in range(cont):
        for j in range(len(Playlist)):
            if id == Playlist[j].getId():
                del Playlist[j]
                cont = cont-1
                break
    Dato = {'message':'Se elimino el dato exitosamente'}
    Respuesta = jsonify(Dato)
    return (Respuesta)

#Eliminar Solicitudes
@app.route('/Solicitudes/<int:pos>', methods=['DELETE'])
def EliminarSol(pos):
    global Solicitudes
    del Solicitudes[pos]
    return jsonify({'message':'Se elimino el dato exitosamente'}) 

#Agregar Usuarios
@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    user = request.json['user']
    contrasena = request.json['contrasena']
    tipo = request.json['tipo']
    encontrado = False
    for us in Usuarios:
        if us.getUser() == user:
            encontrado = True
            break
    if encontrado:
        return jsonify({'message':'Failed','reason':'El usuario ya esta registrado'})
    else:
        Usuarios.append(usuario(nombre,apellido,user,contrasena,tipo))
        return jsonify({'message':'Success','reason':'El usuario se agrego exitosamente'})

#Login
@app.route('/Login', methods=['POST'])
def Logiar():
    global Usuarios
    user = request.json['user']
    contrasena = request.json['contrasena']
    for us in Usuarios:
        if us.getUser() == user and us.getContrasena() == contrasena:
            Dato = {
             'message':'Success',
             'usuario': us.getUser(),  
             'tipo':us.getTipo()
            }
            break
        else:
            Dato = {
             'message':'Failed',
             'usuario': ''  ,  
             'tipo':0
            }
    respuesta = jsonify(Dato)
    return (respuesta)

#Recuperar Contraceña
@app.route('/RecuperarContra', methods=['POST'])
def Recuperar():
    global Usuarios
    use = request.json['user1']
    for Us in Usuarios:
        if use == Us.getUser():
            Dato = {
             'message':'Success',
             'contraseña': 'Su contraseña es: ' +Us.getContrasena()
            }
            break
        else:
            Dato = {
             'message':'Failed',
             'reason': 'El usuario no existe'  
            }
    respuesta = jsonify(Dato)
    return (respuesta)

#Mostrar usuario por nombre
@app.route('/Info', methods=['POST'])
def ObtenerPersona():
    global Usuarios
    user = request.json['user']
    for us in Usuarios:
        if us.getUser() == user:
            Dato = {
                'nombre':us.getNombre(), 
                'apellido':us.getApellido(), 
                'user':us.getUser(),
                'contrasena':us.getContrasena()
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta) 


#Mostrar Cancion
@app.route('/VerCancion', methods=['POST'])
def MostrarCancion():
    global Canciones
    pos = int(request.json['id']) 
    print(pos)
    for us in Canciones:
        if us.getId() == pos:
            Dato = {
                'nombre':us.getNombre(), 
                'artista':us.getArtista(),
                'album':us.getAlbum(), 
                'fecha':us.getFecha(),
                'imagen':us.getImagen(),
                'spotify':us.getSpotify(),
                'youtube':us.getYoutube()
              }
            break
    Respuesta = jsonify(Dato)
    return (Respuesta) 


#Modificar Datos de Usuarios
@app.route('/Actualizar', methods=['PUT'])
def ActuzaliarPersona():
    global Usuarios
    user = request.json['user']
    Buscar = request.json['Buscar']
    usado = False
    for i in range(len(Usuarios)):
        if user == Usuarios[i].getUser() and user != Buscar:
            usado = True
            break
    if usado == False:
        for i in range(len(Usuarios)):
            if Buscar == Usuarios[i].getUser():
                Usuarios[i].setUser(request.json['user'])
                Usuarios[i].setNombre(request.json['nombre'])
                Usuarios[i].setApellido(request.json['apellido'])
                Usuarios[i].setContrasena(request.json['contrasena']) 
                Dato = {'message':'Success', 'reason':'los datos han sido actualizados'}
                break
        for i in range(len(Playlist)):
            if Buscar == Playlist[i].getUser():
               Playlist[i].setUser(request.json['user']) 
    else:
         Dato = {'message':'Failed', 'reason':'El usuario ya esta registrado'}
    Respuesta = jsonify(Dato)
    return (Respuesta)

#Modificar Canciones
@app.route('/ActualizarCan', methods=['PUT'])
def ActuzaliarCanciones():
    global Canciones
    Buscar = int(request.json['Buscar'])
    for i in range(len(Canciones)):
        if Buscar == Canciones[i].getId():
            Canciones[i].setNombre(request.json['nombre'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha']) 
            Canciones[i].setImagen(request.json['imagen']) 
            Canciones[i].setSpotify(request.json['spotify']) 
            Canciones[i].setYoutube(request.json['youtube']) 
            Dato = {'message':'Success', 'reason':'los datos han sido actualizados'}
            break
        else:
            Dato = {'message':'Failed', 'reason':'no se que paso, te juro que si funcionaba'}
    for j in range(len(Playlist)):
        if Buscar == Playlist[j].getId():
            Playlist[i].setNombre(request.json['nombre'])
            Playlist[i].setArtista(request.json['artista'])
            Playlist[i].setAlbum(request.json['album'])
            Playlist[i].setFecha(request.json['fecha']) 
            Playlist[i].setImagen(request.json['imagen']) 
            Playlist[i].setSpotify(request.json['spotify']) 
            Playlist[i].setYoutube(request.json['youtube'])       
    Respuesta = jsonify(Dato)
    return (Respuesta)

#Agregar Solicitud
@app.route('/Solicitud', methods=['POST'])
def AgregarSolicitud():
    global Solicitudes
    nombre = request.json['nombre']
    artista= request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    Solicitudes.append(solicitud(nombre,artista,album,fecha,imagen,spotify,youtube))
    Dato = {
             'message':'Success',
             'reason': 'Su solicitud se ha enviado'  
            }
    respuesta = jsonify(Dato)
    return (respuesta)

#Agregar Canción
@app.route('/Cancion', methods=['POST'])
def AgregarCancion():
    global Canciones, contCancion
    id = contCancion
    nombre = request.json['nombre']
    artista= request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    Canciones.append(cancion(id,nombre,artista,album,fecha,imagen,spotify,youtube))
    contCancion +=1
    Dato = {
             'message':'Success',
             'reason': 'La cancion ha sido agregada'  
            }
    respuesta = jsonify(Dato)
    return (respuesta)

#Aceptar Solicitud
@app.route('/AceptarSol', methods=['POST','DELETE'])
def AceptarSol():
    global Canciones, contCancion, Solicitudes
    pos = int(request.json['pos'])
    id = contCancion
    nombre = Solicitudes[pos].getNombre()
    artista= Solicitudes[pos].getArtista()
    album = Solicitudes[pos].getAlbum()
    fecha = Solicitudes[pos].getFecha()
    imagen = Solicitudes[pos].getImagen()
    spotify = Solicitudes[pos].getSpotify()
    youtube = Solicitudes[pos].getYoutube()
    Canciones.append(cancion(id,nombre,artista,album,fecha,imagen,spotify,youtube))
    contCancion +=1
    Dato = {
             'message':'Success',
             'reason': 'La cancion ha sido agregada'  
            }
    del Solicitudes[pos]
    respuesta = jsonify(Dato)
    return (respuesta)

#Agregar a la playlist
@app.route('/AgPlay', methods=['POST'])
def AgregarPlay():
    global Playlist, Canciones
    id = int(request.json['id'])
    user = request.json['user']
    repetido = True
    for i in range(len(Playlist)):
        if id == int(Playlist[i].getId()) and user == Playlist[i].getUser():
            Dato = {'message':'Failed','reason': 'La cancion ya se encuentra en su playlist' }
            repetido = False
            break
    if repetido:
        for p in Canciones:
            if id == p.getId():
                nombre = p.getNombre()
                artista= p.getArtista()
                album = p.getAlbum()
                fecha = p.getFecha()
                imagen = p.getImagen()
                spotify = p.getSpotify()
                youtube = p.getYoutube()    
                Playlist.append(play(id,user,nombre,artista,album,fecha,imagen,spotify,youtube))
                Dato = {'message':'Success','reason': 'La cancion ha sido agregada' }
                break 
    respuesta = jsonify(Dato)
    return (respuesta)

#Agregar Comentario
@app.route('/Com', methods=['POST'])
def AgregarCometario():
    global Comentarios
    id = request.json['id']
    user = request.json['user']  
    texto = request.json['texto']  
    Comentarios.append(comentario(id,user,texto))
    Dato = {
             'message':'Success',
             'reason': 'El cometario ha sido agregada'  
            }
    respuesta = jsonify(Dato)
    return (respuesta)

if __name__ == "__main__":
    app.run(threaded = True, host = "0.0.0.0", port = 5000, debug = True)