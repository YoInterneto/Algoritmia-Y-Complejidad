
listaPrueba = [3,2,6,9,5,1,7,8,0,4,-33]
listaPrueba1 = [9,8,7,6,5,4,3,2,1,0]


def vector_maxmin(lista):
    """Debido a que el algoritmo tiene que hacer 3/2 n comparaciones
    tendra que ser leida la mitad de la lista 3 veces"""

    medio = int(len(lista)/2)

    #Cogemos un pivote de la lista y comparamos a ambos lados intercabiando la posicion de los
    #elementos, si el elemento de la izquierda de la lista es mayor que el de la derecha
    #1/2n comparaciones
    for posicion in range (medio):
        if(lista[posicion] > lista[(len(lista)-1)-posicion]):
            aux = lista[posicion]
            lista[posicion] = lista[(len(lista)-1)-posicion]
            lista[(len(lista) - 1) - posicion] = aux

    minimo = 99
    maximo = -99

    #Comparamos hasta medio+1 por si la len(lista) es impar, buscando el minimo
    #1/2n comparaciones
    for posicion in range (medio+1):
        if(lista[posicion] < minimo):
            minimo = lista[posicion]

    #Comparamos desde el medio de la lista hasta el final buscando el maximo
    #1/2n comparaciones
    for posicion in range (medio, len(lista)):
        if(lista[posicion] > maximo):
            maximo = lista[posicion]

    #Total -> 3/2n comparaciones

    print("Lista max/min: "+ str(lista) +" - maximo "+ str(maximo) + " minimo "+ str(minimo))

vector_maxmin(listaPrueba)
vector_maxmin(listaPrueba1)
