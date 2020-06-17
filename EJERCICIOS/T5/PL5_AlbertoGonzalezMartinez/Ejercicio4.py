
def movimientoCorrecto(xIni,yIni,xFin,yFin):
    """ Como en el enunciado Mij y Mpq
        i->xIni j->yIni p->xFin q->yFin"""

    #para que el movimiento sea correcto alguna de las dos condiciones se tiene que cumplir
    condicion1 = (abs(xFin-xIni) == 1) and (abs(yFin-yIni) == 2)
    condicion2 = (abs(xFin-xIni) == 2) and (abs(yFin-yIni) == 1)

    return (condicion1 or condicion2)


def mostrarTablero(tablero):
    for lista in tablero:
        print(lista)


def empezarMover(fila, columna, posX, posY):

    tablero = []

    for i in range(fila):
        nuevaFila = []
        for j in range(columna):
            #marcamos desde una principio la posicion de salida la marcamos
            if (i == posX) and (j == posY):
                nuevaFila.append("X")
            else:
                nuevaFila.append("0")
        tablero.append(nuevaFila)

    if movimientoCaballo(tablero, posX, posY, [[posX,posY]]):
        return True
    else:
        print("\nNo se ha encontrado solucion")
        return False


def tableroLleno(tablero, fila, columna):
    lleno = True
    for i in range(fila):
        for j in range(columna):
            if tablero[i][j] == '0':
                lleno = False
    return lleno


def movimientoCaballo(tablero, posX, posY, solucion):

    columnasTablero = len(tablero[0])
    filasTablero = len(tablero)

    # caso base, el caballo ha completado todos lo movimientos del caballo, es decir,
    # el contador de movimientos es igual al numero de casillas
    if tableroLleno(tablero, filasTablero, columnasTablero):
        print("!SE HA ENCONTRADO UNA SOLUCIÓN¡")
        print("Casilla inicial -> "+ str(solucion[0]))
        print("Solucion -> "+ str(solucion))
        print("__Tablero final__")
        mostrarTablero(tablero)
        print("")
        return True
    else:
        #en vez de comprobar todas las posiciones del tablero, unicamente comprobamos las que estan
        #dentro del rango posibles es decir las que estan separadas 2 casillas de la posicion actual
        for fila in range(-2,3):
            for columna in range(-2,3):
                posActualX = posX + fila
                posActualY = posY + columna
                if not ((posActualX >= filasTablero) or (posActualX < 0) or (posActualY >= columnasTablero) or (posActualY <0)):
                    #si el movimiento es correcto y la casilla NO ha sido usada
                    if (movimientoCorrecto(posX, posY, posActualX, posActualY)) and (tablero[posActualX][posActualY] != "X"):

                        tablero[posActualX][posActualY] = "X"
                        solucion.append([posActualX,posActualY])

                        resultado = movimientoCaballo(tablero, posActualX, posActualY, solucion)

                        if resultado:
                            return resultado


empezarMover(5,5,0,0)


