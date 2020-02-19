def esPerfecto(numero):
    suma = 0
    for n in range(1, numero):
        if((numero%n)==0):
            suma += n

    return suma == numero

