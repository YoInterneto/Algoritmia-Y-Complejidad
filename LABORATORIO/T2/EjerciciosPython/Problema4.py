
import random

grafo=[
               [1,2,3,4,5,6,7],
            [1 ,0,3,0,4,0,0,0],
            [2 ,2,0,2,6,4,0,0],
            [3 ,0,2,0,0,5,6,0],
            [4 ,4,6,0,0,3,0,4],
            [5 ,0,4,5,3,0,8,7],
            [6 ,0,0,6,0,8,0,3],
            [7 ,0,0,0,4,7,3,0]
       ]

grafo1=[
               [1,2,3,4,5,6,7],
            [1 ,0,1,0,4,0,0,0],
            [2 ,1,0,2,6,4,0,0],
            [3 ,0,2,0,0,5,6,0],
            [4 ,4,6,0,0,3,0,4],
            [5 ,0,4,5,3,0,8,7],
            [6 ,0,0,6,0,8,0,3],
            [7 ,0,0,0,4,7,3,0]
      ]


def siguienteNodo(camino, grafo):
    minimo = 99
    posicionElegida = -1

    for fila in camino:
        costesNodo = grafo[fila]
        for posicion in range(1, len(costesNodo)):
            costeTemporal = costesNodo[posicion]
            if(costeTemporal != 0):
                if(costeTemporal < minimo):
                    minimo = costeTemporal
                    posicionElegida = fila

    return posicionElegida

def algoritmoPrim(grafo):

    nodoActual = 1
    nodos = len(grafo[0])
    camino = []
    camino.append(nodoActual)
    coste = 0

    while(len(camino) != nodos):

        costesNodo = grafo[nodoActual] #lista con los costes del nodo elegido
        minimo = 99
        posicionElegida = 1

        for posicion in range(1, len(costesNodo)):
            costeTemporal = costesNodo[posicion]
            #si el coste de la arista que se esta mirando es 0 esque es inconexa
            if(costeTemporal != 0):
                #si es menor el coste que el que ya habia se elige una nueva arista
                if(costeTemporal < minimo):
                    minimo = costeTemporal
                    posicionElegida = posicion

        #si ya se ha visitado ese nodo, lo ponemos como inconexo y seguimos con el bucle
        if(posicionElegida in camino):
            costesNodo[posicionElegida] = 0
        #si ese nodo no ha sido visitado y tiene el minimo coste, lo añadimos al camino y sumamos su coste
        else:
            camino.append(posicionElegida)
            coste += costesNodo[posicionElegida]

        print("Camino->", camino ," - coste: ", str(coste))
        nodoActual = siguienteNodo(camino, grafo)

        #si por algun casual la funcion no retorno ningun nodo con el coste minimo se cogera el siguiente nodo
        #de forma aleatoria
        if(nodoActual == -1):
            nodoActual = random.randint(1, nodos)

    print(" ")
    print("** Algoritmo finalizado **")
    print("Camino->", camino ," - coste: ", str(coste))
    print(" \n")


algoritmoPrim(grafo1)
algoritmoPrim(grafo)



