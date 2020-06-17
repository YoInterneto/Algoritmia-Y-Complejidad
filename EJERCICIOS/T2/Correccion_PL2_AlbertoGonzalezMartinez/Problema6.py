
def sumaSoldadas(soldadas):
    suma = 0
    for escalera in soldadas:
        suma += escalera
    return suma

def subirTorre(escaleras, soldadas):
    if(len(escaleras) != 0):
        escaleras.sort()

        escalera1 = escaleras[0]
        escaleras.remove(escalera1)

        escalera2 = escaleras[0]
        escaleras.remove(escalera2)

        soldadura = escalera1 + escalera2
        soldadas.append(soldadura)

        if(len(escaleras) != 0):
            escaleras.append(soldadura)

        subirTorre(escaleras,soldadas)
    else:
        longitudFinal = sumaSoldadas(soldadas)
        print("Se necesitarán "+str(longitudFinal)+" minutos para soldar las escaleras")

escaleras = [8,4,5,6,9,1,2,3,9,5]
subirTorre(escaleras,[])
escaleras1 = [56,27,38,16,54,9,3,12,23,22]
subirTorre(escaleras1,[])