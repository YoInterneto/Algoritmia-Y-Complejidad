
def printMatriz(matriz):
    for fila in matriz:
        print(fila)

def crearMatriz(longitudA, longitudB):

    matriz = []

    #creamos una matriz con longitud [N+1][M+1], para poder operar bien con ella
    for fila in range(longitudA+1):
        filaLista = []
        for columna in range(longitudB+1):
            filaLista.append(0)
        matriz.append(filaLista)

    return matriz

def matrizCoincidencia(cadenaA, cadenaB):

    matriz = crearMatriz(len(cadenaA), len(cadenaB))

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            #saltamos los casos para los cuales la longitud es 0, ya que tienen el valor correspondiente
            if (fila != 0 and columna != 0):
                if(cadenaA[fila-1] == cadenaB[columna-1]):
                    matriz[fila][columna] = matriz[fila-1][columna-1] + 1
                elif(matriz[fila-1][columna] >= matriz[fila-1][columna-1]+1):
                    matriz[fila][columna] = matriz[fila-1][columna]
                else:
                    matriz[fila][columna] = matriz[fila][columna-1]

    return matriz

def subsecuencias(cadenaA, cadenaB):

    matrizFinal = matrizCoincidencia(cadenaA,cadenaB)

    subsecuencia = ""

    #con estas variables obtenemos cuantas vueltas tiene que dar el bucle for
    inicio = abs(len(cadenaA)-len(cadenaB)) + 1
    final = max(len(cadenaB),len(cadenaA))
    iterador = final - inicio

    fila = len(cadenaA)
    columna = len(cadenaB)

    for index in range(iterador+1):

        actual = matrizFinal[fila][columna]
        anterior = matrizFinal[fila-1][columna-1]

        #si dentro de la matriz en la diagonal se produce un cambio de valor, de 8 a 7 por ejemplo,
        #quiere decir, que el bit en la posicion fila-1 o columna-1 de la cadena mas corta, es el que
        #las dos subcadenas tienen en comun
        if(actual > anterior):
            #en este caso la cadena menor seria la cadenaB
            if(fila >= columna):
                bit = cadenaB[columna-1]
                subsecuencia = bit + subsecuencia
            #en este caso sería la cadenaA
            else:
                bit = cadenaA[fila - 1]
                subsecuencia = bit + subsecuencia

        fila -= 1
        columna -= 1


    print("Cadena 1 -> "+ cadenaA +"  -  Cadena 2 -> "+ cadenaB)
    print("Subsecuencia comun -> "+ subsecuencia)
    print("__Matriz__")
    printMatriz(matrizFinal)
    print("\n")



A = "0110101000"
B = "101001001110010"
subsecuencias(A,B)
C = "010"
D = "001"
subsecuencias(C,D)
F = "11101110"
E = "00101"
subsecuencias(E,F)

