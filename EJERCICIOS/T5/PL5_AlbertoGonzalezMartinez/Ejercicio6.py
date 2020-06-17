
tabla = [
    ["b","b","a","d"],
    ["c","a","d","a"],
    ["b","a","c","c"],
    ["d","c","d","b"],
]

indice = ["a","b","c","d"]

resultadoFinal = []


def indiceTabla(letra):

    posicion = -1

    for index in range(len(indice)):
        if letra == indice[index]:
            posicion = index

    return posicion

def reducirCadena(cadena):
    ejecucion = True
    for letra in cadena:
        if letra not in indice:
            ejecucion = False

    if ejecucion:
        reducirCadenaMain(cadena, cadena, len(cadena))
    else:
        print("\nERROR: La cadena no tiene los caracteres esperados [a,b,c,d]")

def reducirCadenaMain(cadena, inicial,longitud):
    #caso base, cuando la cadena es 1
    if len(cadena) == 1:
        global resultadoFinal
        #si la cadena esta dentro de la lista de los resultados encontrados no la printeamos
        if cadena not in resultadoFinal:
            resultadoFinal.append(cadena)
            print("\nSE HA REDUCIDO LA CADENA:")
            print("\tCadena inicial -> "+ inicial)
            print("\tCadena final -> "+ cadena)
            print("\tNumero de pasos -> " + str(longitud))
    else:
        for index in range(len(cadena)-1):
            #cogemos dos letras consecutivas
            letra1 = cadena[index]
            letra2 = cadena[index+1]

            #vemos su posicion
            posLetra1 = indiceTabla(letra1)
            posLetra2 = indiceTabla(letra2)

            #con los indices accedemos a la tabla para hallar la letra que sustituye, y luego concatenamos
            #creando una nueva lista
            letraNueva = tabla[posLetra1][posLetra2]
            cadenaNueva = "".join([cadena[:index], letraNueva, cadena[index+2:]])

            reducirCadenaMain(cadenaNueva,inicial,longitud)


reducirCadena("acaba")
reducirCadena("acabax")
