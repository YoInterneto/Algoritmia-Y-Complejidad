
grafo = {
    1: [(2,5), (4,6)],
    2: [(1,5), (3,9), (5,7)],
    3: [(2,9), (5,9)],
    4: [(1,6), (5,5)],
    5: [(2,7), (4,5), (3,9)]
}

grafo1 = {
    1: [(2,7), (3,9), (6,14)],
    2: [(1,7), (3,10), (4,15)],
    3: [(1,9), (2,10), (4,11), (6,2)],
    4: [(2,15), (3,11), (5,6)],
    5: [(4,6), (6,9)],
    6: [(1,14), (3,2), (5,9)]
}

#funcion que inserta
def insertarNodo(grafo, siguiente, nodosPosibles, camino):
    for nodo, coste in grafo[siguiente]:
        if nodo not in camino:
            nodosPosibles.append((coste, siguiente, nodo))
    nodosPosiblesFinal = nodosPosibles.sort()
    return nodosPosiblesFinal

def imprimirArbol(arbol):
    for(nodo,adyacentes) in arbol.items():
        print(str(nodo)+"->"+str(adyacentes))

def algoritmoPrim(grafo, origen):

    camino = []
    arbol = {}

    #definimos el nodoInicial y lo anadimos a la lista de nodos visitados
    camino.append(origen)

    #insertamos en la lista de posibles los nodos
    nodosPosible = []
    for key, valor in grafo[origen]:
        nodosPosible.append((valor, origen, key))
    nodosPosible.sort()

    while(len(nodosPosible) > 1):
        nodo = nodosPosible.pop(0)
        coste = nodo[0]
        origen = nodo[1]
        siguiente = nodo[2]

        #si el nodo con el minimo coste, no ha sido visitado, es decir, no está dentro del camino seguido,
        #lo añadimos y vemos cuales son los nuevos adyacentes
        if(siguiente not in camino):
            camino.append(siguiente)

            insertarNodo(grafo, siguiente, nodosPosible, camino)

            #si el nodo origen ya está metido dentro del arbol, unicamente tenemos que anadir los nuevos
            #nodos adyacentes encontrados
            if(origen in arbol):
                arbol[siguiente] = [(origen, coste)]
                arbol[origen].append((siguiente, coste))
            #si no, creamos una entrada dentro del arbol
            else:
                arbol[siguiente] = [(origen,coste)]
                arbol[origen] = [(siguiente, coste)]

    print("__Camino__\n"+ str(camino))
    print("__Arbol de recubrimiento__")
    imprimirArbol(arbol)

print("GRAFO 1")
algoritmoPrim(grafo, 1)
print("\nGRAFO 2")
algoritmoPrim(grafo1, 1)