import random

n=[4,5,2,8,9,3,1,6,7]

def min_max(lista):
    for i in range (int(len(lista)/2)):#Cambiamos cada valor por su simetrico si el de la mitad izquierda                                
        izquierdo=lista[i]              #es mayor para dejar los menores a la izquierda
        derecho=lista[len(lista)-i-1]   #y los mayores a la derecha
        if(izquierdo>derecho):
           lista[i]=derecho
           lista[len(lista)-i-1]=izquierdo
           
    minimo=lista[0]      #minimo de la primera mitad
    for i in range (int(len(lista)/2)+1):#sumamos 1 por si la longitud es impar
        if(lista[i]<minimo):
            minimo=lista[i]
    
    maximo=lista[0]     #maximo de la segunda mitad
    for i in range((int(len(lista)/2)),len(lista)):
        if(lista[i]>maximo):
            maximo=lista[i]
    retorno="Lista dividida: " + str(lista) +" Maximo: " +str(maximo)+" Minimo: "+str(minimo)
    return retorno

print(min_max(n))




#99 es el infinito, es decir, no hay conexion entre los nodos
matriz_costes=[[1,2,3,4,5,6,7],
            [3,99,3,99,4,99,99,99],
            [2,2,99,2,6,4,99,99],
            [3,99,2,99,99,5,6,99],
            [4,4,6,99,99,3,99,4],
            [5,99,4,5,3,99,8,7],
            [6,99,99,6,99,8,99,3],
            [7,99,99,99,4,7,3,99]]

matriz_costes2=[[1,2,3,4,5,6,7],
            [1,99,1,99,4,99,99,99],
            [2,1,99,2,6,4,99,99],
            [3,99,2,99,99,5,6,99],
            [4,4,6,99,99,3,99,4],
            [5,99,4,5,3,99,8,7],
            [6,99,99,6,99,8,99,3],
            [7,99,99,99,4,7,3,99]]

"""funcion auxiliar para saber que nodo
tiene el minimo coste con sus nodos conexos
"""
def posicionMinimo(matriz,listaVisitados):
    minimo=matriz[1][1]
    for i in listaVisitados:
        for j in range(1,int(len(matriz[i]))):
            if(minimo>matriz[i][j]):
                minimo=matriz[i][j]
                posicion=i
    return posicion            


def prim(n,matriz):#n es el numero de nodos
    actual=random.randint(1, n)#coge de inicio un numero random
    print("Nodo inicial: ",actual)
    camino=[actual]#el camino que seguiremos donde introduciremos el nodo inicial
    cont=0
    posicion=0
    coste=0
    while(cont!=n-1):
        minimo=matriz[actual][1] #la posicion del primer coste
        posicion=1 #al empezar a comprobar el minimo desde el primer coste, puede que no entre al if porque el minimo este en la posicion 1
        for i in range(1,int(len(matriz[actual]))):
            if(minimo>matriz[actual][i]): #comprobamos el minimo de la fila
                minimo=matriz[actual][i]
                posicion=i #guardamos la posicion del minimo para ver con que nodo conecta
        if(posicion in camino):#si ya se ha visitado el nodo
            matriz[actual][posicion]=99#si ya ha sido visitado se pone 99 en la posicion
        else:
            cont+=1
            print("Se unen los nodos: ",matriz.index(matriz[actual])," y ",posicion)
            coste+=matriz[actual][posicion] #sumamos el coste de la conexion
            print("Coste actual: ", coste)
            camino.append(posicion) #insertamos el nodo visitado en el camino
        print("Camino actual: ",camino)
        #se comprueba cual es el nodo visitado que tiene el valor minimo
        actual=posicionMinimo(matriz,camino)#saber minimo de todos los visitados
    retorno= "Camino: "+str(camino)+" con coste: "+str(coste)
    
    return retorno
    

print(prim(7,matriz_costes2))
#print(1 in matriz_costes)

"""def prim(n,matriz):#n es el numero de nodos
    actual=random.randint(1, n)#coge de inicio un numero random
    camino=[actual]
    cont=0
    posicion=0
    coste=0
    while(cont!=n-1):
        print("cont:",cont)
        print("act",actual)
        minimo=matriz[actual][1]#la posicion del primer coste
        posicion=1
        for i in range(1,int(len(matriz[actual]))):
                
            print("i: ",i,"long: ",(matriz[actual]),(matriz[actual][i]))
 
            if(minimo>matriz[actual][i]):
                minimo=matriz[actual][i]
                
                posicion=i
                
                
            
        print("minimo",minimo)
        print("pos",posicion)
        if(posicion in camino):#si ya se ha visitado el nodo
            
            print("nposicion",matriz[actual][posicion])
            print("esta",posicion in camino)
            matriz[actual][posicion]=99
            print(matriz[actual][posicion])
        else:
            cont+=1
            print("Se unen los nodos: ",matriz.index(matriz[actual])," y ",posicion)
            coste+=matriz[actual][posicion]
            camino.append(posicion)
            actual=posicion
        print(camino)
        print(coste)
        actual=posicionMinimo(matriz,camino)
        #saber minimo de todos los visitados
        """"""for i in range (1,int(len(camino))):
            numero = camino[i]
            minimoAux=matriz[numero][1]
            if(minimoAux>matriz[numero][i]):
                print("posicionMinimo",matriz[numero][i])""""""
                

    
    
    return camino
    

print(prim(7,matriz_costes))"""








