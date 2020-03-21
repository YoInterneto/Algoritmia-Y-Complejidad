
escaleras = [8,4,5,6,9,1,2,3,9,5]

def subirTorre(escaleras):

    contador = 0
    minutos = 0
    longitud = 0

    while(contador != len(escaleras)):
        l = escaleras[contador]
        minutos += minutos + l
        longitud += l
        contador += 1

    print("Para soldar", len(escaleras) ,"escaleras se ha tardado", minutos ,"min (longitud:", longitud,"m)")

#La segunda llamada a funcion es para demostrar que es mucho mas optimo hacerlo con la lista ordenada de menor a mayor
#que hacerlo con la lista desordenada o ordenada de mayor a menor
escaleras.sort()
print("Optimo")
subirTorre(escaleras)
escaleras.sort(reverse=True)
print("No optimo")
subirTorre(escaleras)