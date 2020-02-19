def sumatorio(numero):
    if(numero==0):
        return 0;
    else:
        return numero + sumatorio(numero-1)

