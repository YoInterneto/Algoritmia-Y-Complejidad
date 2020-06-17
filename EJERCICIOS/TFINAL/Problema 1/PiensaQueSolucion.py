
from random import sample
from random import randrange

def txtSolucion(usuarios, grupos, nUsuarios, index, opcion):

    solucion = open("solucion_voraz.txt",opcion)
    solucion.writelines("**** SOLUCION "+ str(index) +" **** \n")
    solucion.write("  Nº grupos -> "+ str(len(grupos)) +"\n")
    solucion.write("  Nº usuarios -> "+ str(nUsuarios) +"\n")
    solucion.write("  ID usuarios -> " + str(usuarios) + "\n")
    solucion.write("  Grado de conexión -> "+ str(round(len(grupos)/nUsuarios, 3)) + "\n")
    print(round(len(grupos)/nUsuarios, 3))
    ngrupo = 1
    for grupo in grupos:
        if ngrupo < 10:
            solucion.write("   Grupo " + str(ngrupo) + " ->  " + str(grupo) + " \n")
        else:
            solucion.write("   Grupo " + str(ngrupo) + " -> " + str(grupo) + " \n")
        ngrupo += 1
    solucion.write("\n")
    solucion.close()


def formarGrupos(diccionario, usuariosLista):

    # Esta lista se utilizara para ver que usuarios ya estan conectados, es decir, los que pertencen a un grupo
    usuariosConectados = []
    # Esta lista guarda una cola de los contactos los cuales tenemos que buscar sus conocidos
    siguienteUsuario = []
    # Guarda una lista por cada grupo y los integrantes de ese grupo
    usuarioGrupo = []

    for usuario in usuariosLista:
        if usuario not in usuariosConectados:

            nuevoGrupo = []
            nuevoGrupo.append(usuario)

            #metemos el usuario en la lista para deja constacia de que ya hemos comprobado sus amigos
            usuariosConectados.append(usuario)

            siguienteUsuario.append(usuario)

            #mediante este bucle, comprobaremos cuantas personas estan en el grupo de amigos de
            #la persona que queremos
            while len(siguienteUsuario) != 0:

                siguiente = siguienteUsuario[0] #usuario de la lista de "abiertos"
                amigos = diccionario.get(siguiente)

                #amigos no reciprocos, es decir, que el usuario que se está comprobando no lo tiene pero otro del diccionario
                #si que lo tiene
                for persona in usuariosLista:
                    if siguiente in diccionario.get(persona):
                        #solo lo metemos si no tiene grupo ya o no ha sido comprobado
                        if persona not in siguienteUsuario and persona not in usuariosConectados:
                            siguienteUsuario.append(persona)
                            usuariosConectados.append(persona)
                            nuevoGrupo.append(persona)

                #con el none vemos que el siguiente usuario a comprobar sea de los N elegidos para la,prueba, es decir, este dentro del diccionario
                if amigos is not None:
                    for amigo in amigos:
                        if amigo not in siguienteUsuario and amigo not in usuariosConectados:
                            siguienteUsuario.append(amigo)
                            usuariosConectados.append(amigo)
                            nuevoGrupo.append(amigo)

                siguienteUsuario.remove(siguiente)

            usuarioGrupo.append(nuevoGrupo)

    return (usuarioGrupo,len(usuariosConectados))

def gradoConexion(nUsuarios):

    archivo = open("ejemplo_voraz.txt")

    entradas = []
    listaUsuarios = []

    diccionario = {}

    for linea in archivo:
        entradas.append(linea)

    listaElegidos = sample(entradas,nUsuarios)

    for index in range(len(listaElegidos)):
        usuario = listaElegidos[index]

        llaveValor = usuario.split(":")

        llave = llaveValor[0]
        valor = llaveValor[1].split(",")

        listaUsuarios.append(llave)

        valorFinal = []

        # el valor se divide por ","
        for conocido in valor:
            # si tenemos el valor "_" de nombre quiere decir que no tiene conocidos
            if "_" not in conocido:
                if "\n" in conocido:
                    conocido = conocido.replace("\n", "")
                valorFinal.append(conocido)

        diccionario[llave] = valorFinal

    grupos = formarGrupos(diccionario, listaUsuarios)
    txtSolucion(listaUsuarios, grupos[0], grupos[1], 1, "w")

#funcion que crea el diccionario
def cargaDatos():

    archivo = open("ejemplo_voraz.txt","w")

    for usuario in range(1,2501):
        #como mucho 3 conocidos por persona
        conocidos = randrange(0,4)
        listaConocidos = ""
        if conocidos == 0:
            listaConocidos += "_"
        else:
            #creamos la lista de personas que conoce el usuario
            for conocido in range(conocidos):
                #si es el final de la lista de conocidos no ponemos la coma al final
                if conocido == conocidos-1:
                    usuarioConocido = randrange(1,2501)
                    while str(usuarioConocido) in listaConocidos:
                        usuarioConocido = randrange(1,2001)
                    listaConocidos += str(usuarioConocido)
                #si no es el final ponemos la coma
                else:
                    usuarioConocido = randrange(1,2501)
                    while str(usuarioConocido) in listaConocidos:
                        usuarioConocido = randrange(1,2501)
                    listaConocidos += str(usuarioConocido) + ","

        entradaDiccionario = str(usuario) + ":" + listaConocidos

        if usuario == 2500:
            archivo.write(entradaDiccionario)
        else:
            archivo.write(entradaDiccionario + "\n")

    archivo.close()


if __name__ == '__main__':
    #cargaDatos() #solo si se quiere volver a crear nuevos datos
    gradoConexion(100)

