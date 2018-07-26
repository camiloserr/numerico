import math
#defina el rango en el cual la funcion es creciente y tiene una raiz
def creciente( low , high ):
    x = (high + low)/2
    y = funcion(x)
    if( y > -0.00001 and y<0.00001):
        return x
    if(y > 0):
        return creciente( low , x )
    else:
        return creciente ( x , high )

#defina el rango en el cual la funcion es decreciente y tiene una raiz
def decreciente( low , high ):
    x = (high + low)/2
    y = funcion(x)
    if( y > -0.00001 and y<0.00001):
        return x
    if(y < 0):
        return decreciente( low , x )
    else:
        return decreciente ( x , high )



#defina la funcion
def funcion(x):
    return (math.e ** -x) +x -2


print (creciente ( 0 , 100 ))
