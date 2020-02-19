from esPrimo import esPrimo
from esPerfecto import esPerfecto

def primosPerfectos():
    numero = int(input("Escriba un número: "))
    nPrimos = 0
    nPerfectos = 0

    for n in range(1,numero+1):
        if(esPrimo(n)): nPrimos += 1
        if(esPerfecto(n)): nPerfectos += 1

    print("Números primos: ", nPrimos)
    print("Números perfectos: ", nPerfectos)


primosPerfectos()