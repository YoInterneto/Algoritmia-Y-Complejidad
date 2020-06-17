

def txtSolucion(notas, suma, opcion, index):

    solucion = open("solucion_dyv.txt",opcion)
    solucion.writelines("**** SOLUCION "+ str(index) +"**** \n")
    solucion.write("  Notas -> "+ str(notas) +"\n")
    solucion.write("  Suma total -> "+ str(round(suma,3)) +"\n")
    solucion.write("  Nota media -> "+ str(round(suma/len(notas),3)) +"\n")
    solucion.write("\n")
    solucion.close()

def sumaNotas(notas):
    #solo queda una nota en la lista, con lo cual retornamos esa nota para sumarla
    if len(notas) == 1:
        nota = notas[0]
        return nota
    #lista vacía
    elif len(notas) == 0:
        return -1
    else:
        mitadLista = len(notas) // 2

        suma = (sumaNotas(notas[:mitadLista]) + sumaNotas(notas[mitadLista:]))
        return suma

def calcularMedia():

    archivo = open("ejemplo_dyv.txt")
    index = 1

    for lineas in archivo:
        notas = lineas.split("//")
        listaNotas = []

        for nota in notas:
            listaNotas.append(float(nota))

        if index == 1:
            txtSolucion(listaNotas, sumaNotas(listaNotas), "w", index)
        else:
            txtSolucion(listaNotas, sumaNotas(listaNotas), "a", index)

        index += 1

if __name__ == '__main__':
    calcularMedia()