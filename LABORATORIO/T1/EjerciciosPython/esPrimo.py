def esPrimo(numero):
    # Si el numero es negativo NO será primo
    if (numero <= 0):
        return False
    else:
        for n in range(2, numero):
            if ((numero % n) == 0):
                return False
        return True
