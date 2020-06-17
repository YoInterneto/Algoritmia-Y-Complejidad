

def comparar(pivote, lista, estaLista, menores, mayores, index):
    #si esta vacía retornamos el resultado
    if(len(lista) <= index):
        return (estaLista,menores,mayores)
    else:
        elemento = lista[index]

        if (elemento == pivote):
            estaLista = True
        elif (elemento > pivote):
            mayores.append(elemento)
        else:
            menores.append(elemento)

        return comparar(pivote, lista, estaLista, menores, mayores, index+1)

def ponerCorcho(corchos,botellas):

    if len(corchos) != len(botellas):
        print("ERROR: Las listas no son iguales")
    else:
        botella = botellas[0]

        resultadoCorchos = comparar(botella, corchos, False, [], [], 0)
        estaListaCorcho = resultadoCorchos[0]
        corchosMenores = resultadoCorchos[1]
        corchosMayores = resultadoCorchos[2]

        #si no se encuentra el corcho para la botella, no seguimos con la ejecución
        if not estaListaCorcho:
            print("ERROR: No se ha encontrado corcho para la botella "+ str(botella))
        else:
            corcho = botella
            resultadoBotellas = comparar(corcho, botellas, False, [], [], 0)
            botellasMenores = resultadoBotellas[1]
            botellasMayores = resultadoBotellas[2]

            listaFinal = [[botella,corcho]]

            print("Se han encontrado coincidencias -> corcho ("+ str(corcho) +") - botella ("+ str(botella) +")")
            print("\tcorchos -> "+ str(corchos) +" - botellas -> "+ str(botellas))

            botellas.remove(botella)

            if len(corchosMenores) != 0:
                listaFinal.append(ponerCorcho(corchosMenores, botellasMenores))
            if len(corchosMayores) != 0:
                listaFinal.append(ponerCorcho(corchosMayores, botellasMayores))

            return listaFinal


corchos = [3,6,66,1,2,9,20,4,5]
botellas =[7,20,4,1,2,3,9,6,5]
ponerCorcho(corchos, botellas)
corchos1 = [3,6,7,1,2,9,20,4,5]
botellas1 =[7,20,4,1,2,3,9,6,5]
