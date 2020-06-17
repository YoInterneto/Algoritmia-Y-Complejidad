
from random import randrange

grafo = [
    [0  , 1  , 999, 999, 999, 1  , 999],
    [999, 0  , 1  , 1  , 1  , 999, 999],
    [999, 999, 0  , 999, 999, 999, 999],
    [999, 999, 1  , 0  , 999, 999, 999],
    [999, 1  , 999, 1  , 0  , 999, 999],
    [1  , 1  , 999, 999, 1  , 0  , 999],
    [1  , 999, 999, 999, 999, 1  , 0  ]
]

def pesoAristas(grafo):

    for fila in range(len(grafo)):
        for columna in range(len(grafo[fila])):
            #si la arista esta conectada a otro nodo cremos un valor aleatorio de peso para esa arista
            if grafo[fila][columna] == 1:
                #caso para el cual dos aristas son simetricas (i,j)=(j,i), y la arista simetrica ya tiene su coste aleatorio dado
                #es decir, cuando j<i ya que querra decir que la fila del nodo simetrico se ha comprobado antes que la del nodo actual
                if columna < fila and grafo[columna][fila] != 0 and grafo[columna][fila] != 999:
                    grafo[fila][columna] = grafo[columna][fila]
                else:
                    grafo[fila][columna] = randrange(1,11)

    return grafo


#esta funcion nos muestra la matriz y además nos muestra que aristas estan siendo comprobadas en cada
#momento
def mostrarGrafo(grafo, pos1, pos2, pos3):

    final = ""
    cabecera = "     "

    for fila in range(len(grafo)):
        cabecera += "N" + str(fila+1) + "     "
        linea = "N" + str(fila+1) + "  "
        for columna in range(len(grafo[fila])):
            posAux = (fila, columna)
            coste = grafo[fila][columna]
            if posAux == pos1 or posAux == pos2 or posAux == pos3:
                if coste == 999:
                    linea += ">"+ "-" + "<    "
                elif coste > 99:
                    linea += ">"+ str(coste) + "<  "
                elif coste < 10:
                    linea += ">"+ str(coste) + "<    "
                else:
                    linea += ">"+ str(coste) + "<   "
            else:
                if coste == 999:
                    linea += " "+ "-" + "     "
                elif coste > 99:
                    linea += " "+ str(coste) + "   "
                elif coste < 10:
                    linea += " "+ str(coste) + "     "
                else:
                    linea += " "+ str(coste) + "    "
        final += linea + "\n"
    cabecera += "\n"

    print(cabecera+final)


def algoritmoFloyd(grafo):

    grafoFinal = grafo

    longitud = len(grafoFinal)

    iteracion = 1

    #para la iteracion k se comprueba que haya que para cada par de nodos [i][j], exista
    #un camino minimo que vaya de i hasta j pasando por k
    for k in range(longitud):
        for i in range(longitud):
            #comprobamos si el elemento intersección de la columna y la fila (i,j), es mayor
            #que la suma de los costes de los elementos que estemos sumando y pondremos el camino minimo de los dos
            for j in range(longitud):
                coste1 = grafoFinal[i][j]
                coste2 = grafoFinal[i][k]+grafoFinal[k][j]

                grafoFinal[i][j] = min(coste1,coste2)

                #mostramos el grafo y seguimos iterando
                print("\nITERACION ["+ str(iteracion) + "]")
                mostrarGrafo(grafoFinal, (i,j), (i,k), (k,j))
                iteracion += 1

    return grafoFinal


algoritmoFloyd(pesoAristas(grafo))
