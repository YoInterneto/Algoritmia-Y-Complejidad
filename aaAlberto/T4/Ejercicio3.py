
def pagar(billetes,nbilletes,cantidad):

    if len(nbilletes) != len(billetes):
        print("ERROR: ")
    elif (len(nbilletes) or len(billetes)) == 0:
        print("ERROR: ")
    else:
        usados = []

        #como esta ordenado de menor a mayor y queremos pagar con el mínimo de billetes, tendremos
        #que empezar por el final de la lista
        for index in range(len(billetes)-1,-1, -1):
            billeteValor = billetes[index]
            print(billeteValor)
            while (nbilletes[index] > 0) & (cantidad > 0) & (billeteValor <= cantidad):
                cantidad -= billeteValor
                usados.append(billeteValor)
                nbilletes[index] -= 1
        print(usados)

        if(cantidad > 0):
            print("No has podido pagar")
        else:
            print("Si se ha podido pagar")

billetes = [1,2,5,10,20,50]
nbilletes = [3,6,4,3,1,1]
pagar(billetes,nbilletes,101)