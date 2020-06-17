
soluciones = []

listaAbiertos = []

#escribe la solucion en el txt
def txtSolucion(opcion, nLaberinto):
    global soluciones

    archivo = open("solucion_backtracking.txt", opcion)

    index = 1

    archivo.write("#####################################\n")
    archivo.write("############ LABERINTO "+ str(nLaberinto) +" ############\n")
    archivo.write("#####################################\n")

    for solucion in soluciones:
        if index == 1:
            archivo.writelines(" >SOLUCION OPTIMA< \n")
        else:
            archivo.writelines(" >SOLUCION " + str(index) + "< \n")
        archivo.write("  Nº de pasos -> " + str(len(solucion)) + "\n")
        archivo.write("  Pasos -> \n" + escribirPasos(solucion) + "\n")
        archivo.write("\n")
        index += 1
    archivo.close()

#retorna una cadena con todos los pasos
def escribirPasos(solucion):

    cadenaFinal = ""

    cadenaFinal += "   *Posicion inicial [" + str(solucion[0][0]) + "," + str(solucion[0][1]) + "]\n"

    for paso in solucion[1:len(solucion)-1]:
        direccion = paso[0]
        posX = paso[1][0]
        posY = paso[1][1]

        if direccion == "r":
            cadenaFinal += "    -continuamos recto hasta [" + str(posX) + "," + str(posY) + "]\n"
        else:
            cadenaFinal += "    -giramos a derecha hasta [" + str(posX) + "," + str(posY) + "]\n"

    cadenaFinal += "   *Posicion final [" + str(solucion[len(solucion)-1][0]) + "," + str(solucion[len(solucion)-1][1]) + "]\n"

    return cadenaFinal

#lee los laberintos del txt y los comprueba
def leerMapa():

    global soluciones

    archivo = open("ejemplo_backtracking.txt", "r")

    entrada = []
    problema = []

    for linea in archivo:
        #nuevo laberinto
        if linea.startswith("*"):
            entrada.append(problema)
            problema = []
        else:
            problema.append(linea)
    entrada.append(problema)

    index = 1

    for laberinto in entrada:
        nFilas = int(laberinto[0])
        nColumnas = int(laberinto[1])

        informacionMapa = crearMapa(laberinto[2:], nFilas, nColumnas)

        mapa = informacionMapa[0]
        filaInicial = informacionMapa[1]
        columnaInicial = informacionMapa[2]

        direccion = direccionSalida(mapa, filaInicial, columnaInicial)

        if direccion == "error":
            print("ERROR: No se puede salir de la casilla de salida")
        else:
            encontrarCamino(mapa, direccion, filaInicial, columnaInicial, [[filaInicial, columnaInicial]])

            soluciones.sort(key=len)

            if index == 1:
                txtSolucion("w", index)
            else:
                txtSolucion("a", index)

            soluciones = []

            index += 1

#crea la matriz del mapa, con las casillas 0 = 3, y retorna donde esta el 1, el inicio
def crearMapa(laberinto, nFilas, nColumnas):

    mapa = []

    filaInicial = -1
    columnaInicial = -1

    for fila in range(nFilas):
        datos = laberinto[fila].split("\t")
        calle = []
        for columna in range(nColumnas):
            dato = datos[columna]
            #quitamos los caracteres finales
            if "\n" in dato:
                dato = dato.replace("\n", "")
            #si es uno apuntamos las coordenadas de la casillas de salida
            if dato == "1":
                filaInicial = fila
                columnaInicial = columna
            #en la casillas libres ponemos un 3 para luego poder sumar las veces que se pasan por ella sin problemas
            elif dato == "0":
                dato = "3"
            calle.append(dato)
        mapa.append(calle)

    return [mapa, filaInicial, columnaInicial]

#retorna la direccion hacia la que tiene que salir, en caso de haber varias retorna la ultima
def direccionSalida(mapa, fila, columna):

    direccion = "error"

    #SUR
    if (fila + 1) < len(mapa) and (fila + 1) >= 0 and columna < len(mapa[0]) and columna >= 0:
        if mapa[fila+1][columna] != "x":
            direccion = "sur"
    #NORTE
    if (fila - 1) < len(mapa) and (fila - 1) >= 0 and columna < len(mapa[0]) and columna >= 0:
        if mapa[fila - 1][columna] != "x":
            direccion = "norte"
    #ESTE
    if fila < len(mapa) and fila >= 0 and (columna + 1) < len(mapa[0]) and (columna + 1) >= 0:
        if mapa[fila][columna + 1] != "x":
            direccion = "este"
    #OESTE
    if fila < len(mapa) and fila >= 0 and (columna - 1) < len(mapa[0]) and (columna - 1) >= 0:
        if mapa[fila][columna - 1] != "x":
            direccion = "oeste"

    return direccion

#calcula la direccion, ademas de la nueva posicion desopues de seguir recto o girar a la derecha
def calcularDireccion(direccionActual, posFila, posColumna, movimiento):
    direccionFinal = ""

    if movimiento == "r":
        if direccionActual == "norte":
            posFila -= 1
            direccionFinal = direccionActual
        elif direccionActual == "sur":
            posFila += 1
            direccionFinal = direccionActual
        elif direccionActual == "este":
            posColumna += 1
            direccionFinal = direccionActual
        elif direccionActual == "oeste":
            posColumna -= 1
            direccionFinal = direccionActual
    elif movimiento == "d":
        if direccionActual == "norte":
            posColumna += 1
            direccionFinal = "este"
        elif direccionActual == "sur":
            posColumna -= 1
            direccionFinal = "oeste"
        elif direccionActual == "este":
            posFila += 1
            direccionFinal = "sur"
        elif direccionActual == "oeste":
            posFila -= 1
            direccionFinal = "norte"

    return [direccionFinal, posFila, posColumna]

#suma 1 a la casilla por la que hemos pasado para saber cuantas veces se pasa por una casilla
def mapaNuevo(mapaViejo, posX, posY):

    mapaFinal = []

    for fila in range(len(mapaViejo)):
        filaNueva = []
        for columna in range(len(mapaViejo[0])):
            #sera la casilla a la que sumaremos uno
            if fila == posX and columna == posY:
                if int(mapaViejo[fila][columna]) != 2:
                    nuevo = str(int(mapaViejo[fila][columna]) + 1)
                    filaNueva.append(nuevo)
                else:
                    nuevo = mapaViejo[fila][columna]
                    filaNueva.append(nuevo)
            else:
                nuevo = mapaViejo[fila][columna]
                filaNueva.append(nuevo)

        mapaFinal.append(filaNueva)

    return mapaFinal

#retorna una nueva lista con el elemento indexado
def solucionNueva(solucionVieja, nuevo):

    solucionFinal = []

    for dato in solucionVieja:
        solucionFinal.append(dato)
    solucionFinal.append(nuevo)

    return solucionFinal

#el mapa es la lista con el camino realizado hasta ahora, la direccion es hacia donde mira el camion,
#posFila y posColumna es la posicion actual y solucion el camino
def encontrarCamino(mapa, direccion, posFila, posColumna, solucion):

    global soluciones
    global listaAbiertos

    if mapa[posFila][posColumna] == "2":
        print("SE HA ENCONTRADO SOLUCION")

        solucion.append([posFila, posColumna])
        soluciones.append(solucion)

        #seguimos buscando soluciones
        if len(listaAbiertos) != 0:
            siguiente = listaAbiertos.pop(0)
            encontrarCamino(siguiente[0], siguiente[1], siguiente[2], siguiente[3], siguiente[4])
    else:
        #MOVIENTO A LA DERECHA
        #calculamos la direccion y nueva posicion
        informacionD = calcularDireccion(direccion, posFila, posColumna, "d")
        nuevaDireccionD = informacionD[0]
        posFilaD = informacionD[1]
        posColumnaD = informacionD[2]

        nodoAbiertoD = []

        #si no se sale de los limites del mapa
        if posFilaD < len(mapa) and posFilaD >= 0 and posColumnaD < len(mapa[0]) and posColumnaD >= 0:
            #para no repetir soluciones, es decir, que sea la misma pero dando vueltas tod el rato, comprobamos
            #que nunca haya realizado ese movimiento antes
            if mapa[posFilaD][posColumnaD] != "x" and ["d",[posFilaD,posColumnaD], nuevaDireccionD] not in solucion:
                nuevoMapaD = mapaNuevo(mapa, posFilaD, posColumnaD)

                solucionD = solucionNueva(solucion, ["d",[posFilaD,posColumnaD], nuevaDireccionD])

                nodoAbiertoD = [nuevoMapaD, nuevaDireccionD, posFilaD, posColumnaD, solucionD]

        #MOVIMIENTO RECTO
        #calculamos la direccion y nueva posicion
        informacionR = calcularDireccion(direccion, posFila, posColumna, "r")
        nuevaDireccionR = informacionR[0]
        posFilaR = informacionR[1]
        posColumnaR = informacionR[2]

        nodoAbiertoR = []

        #si no se sale de los limites del mapa
        if posFilaR < len(mapa) and posFilaR >= 0 and posColumnaR < len(mapa[0]) and posColumnaR >= 0:
            # para no repetir soluciones, es decir, que sea la misma pero dando vueltas tod el rato, comprobamos
            # que nunca haya realizado ese movimiento antes
            if mapa[posFilaR][posColumnaR] != "x" and ["r",[posFilaR,posColumnaR], nuevaDireccionR] not in solucion:
                nuevoMapaR = mapaNuevo(mapa, posFilaR, posColumnaR)

                solucionR = solucionNueva(solucion, ["r", [posFilaR, posColumnaR], nuevaDireccionR])

                nodoAbiertoR = [nuevoMapaR, nuevaDireccionR, posFilaR, posColumnaR, solucionR]

        if len(nodoAbiertoR) != 0:
            listaAbiertos.insert(0, nodoAbiertoR)
        if len(nodoAbiertoD) != 0:
            listaAbiertos.insert(0, nodoAbiertoD)

        if len(listaAbiertos) != 0:
            siguiente = listaAbiertos.pop(0)
            encontrarCamino(siguiente[0], siguiente[1], siguiente[2], siguiente[3], siguiente[4])
        else:
            print("No se puede continuar la ejecucion")

if __name__ == '__main__':
    leerMapa()