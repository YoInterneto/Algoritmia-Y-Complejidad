def es_primo(n):
    cont=0
    for i in range(2,n-1,1):
        if((n%i==0)):
            return False
    return True;

def es_perfecto(n):
    sumatorio=0
    for i in range(1,n-1,1):
        if((n%i==0)):
            sumatorio+=i
    return sumatorio==n

def primos_perfectos():
    n=int(input("Introduzca hasta que numero quiere saber los primos y perfectos: "))
    primos=0
    perfectos=0
    for i in range(1,n+1,1):
        if(es_primo(i)):
            primos+=1
        if(es_perfecto(i)):
            perfectos+=1
    print("Numero de primos: ", primos)
    print("Numero de perfectos: ",perfectos)


            


def sumatorio(n):
    if(n==0):
        return 0;
    else:
        return n + sumatorio(n-1)






