

def encontrarRio(inicio, fin, error):

    distanciaPuente = fin - inicio

    #si la distancia es mayor que el error de estimación seguimos comprobando
    if(distanciaPuente > error):
        #dividimos la distancia en tercios para poder utilizar um algoritmo divide y venceras
        tercio = distanciaPuente/3

        #como el valle es una curva, utilizamos la funcion de una curva, para calcular el inicio de cada
        #uno de los tercios
        alturaTercio2 = (inicio+ tercio) **2
        alturaTercio3 = (inicio+ (fin-tercio)) **2

        #vemos cual de las partes del puente es mas profunda
        if alturaTercio2 > alturaTercio3:
            return encontrarRio(inicio+tercio, fin, error)
        else:
            return encontrarRio(inicio, fin - tercio, error)
    #si la distancia es menor que el error devolvemos donde tirarnos
    else:
        posicionElegida = inicio
        for posicion in range(int(distanciaPuente)):
            if posicion**2 < posicionElegida**2:
                posicionElegida = posicion
        return posicionElegida

print(encontrarRio(220,0,4))
print(encontrarRio(-30,120,6))