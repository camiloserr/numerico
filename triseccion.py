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
    if( y > -0.0000001 and y<0.0000001):
        return x
    if(y < 0):
        return decreciente( low , x )
    else:
        return decreciente ( x , high )


#triseccion para funciones  con una raiz en el rango (low , high)
def tri(low , high):
    tamano = (high - low) / 3
    x1 = low + tamano
    x2 = low + 2*tamano

    #evalua la funcion en la mitad
    y = funcion ( (low + high )/2)
    if (y > -0.0000001 and y < 0.0000001):
        return ((low + high)/2)


    #si la funcion cambia de signo en la primera particion, mando la recursion por ahi
    if( funcion (low ) * funcion (x1 ) < 0):
        return tri (low , x1)

    if (funcion(x1) * funcion(x2) < 0):
        return tri(x1, x2)

    if (funcion(x2) * funcion(high) < 0):
        return tri(x2 , high)

    else:
        return "error inesperado"


def cua(low , high):
    tamano = (high - low) / 4
    x1 = low + tamano
    x2 = low + 2 * tamano
    x3 = low + 3 * tamano

    # evalua la funcion en la mitad
    y = funcion((low + high) / 2)
    if (y > -0.0000001 and y < 0.0000001):
        return ((low + high) / 2)

    # si la funcion cambia de signo en la primera particion, mando la recursion por ahi
    if (funcion(low) * funcion(x1) < 0):
        return cua(low, x1)

    if (funcion(x1) * funcion(x2) < 0):
        return cua(x1, x2)

    if (funcion(x2) * funcion(x3) < 0):
        return cua(x2, x3)

    if (funcion(x3) * funcion(high) < 0):
        return cua(x3, high)

    else:
        return "error inesperado"


def general(low , high , particiones):

    #caso base
    y = funcion((low + high) / 2)
    #calcula la funcion en el punto medio de la particion
    if (y > -0.000000001 and y < 0.000000001):
        return ((low + high) / 2)
    #se crea el tamaño de cada particion
    tamano = (high - low) / particiones
    for i in range(particiones):
        x1 = low + i*tamano
        x2 = low +(i+1)*tamano
        #si la funcion cambi de signo en esa particion, manda la recursion
        if( funcion (x1) * funcion(x2) < 0):
            return general(x1 , x2 , particiones)


    return "error inseperado"

#defina la funcion
def funcion(x):
    return (math.e ** -x) +x -2


print ("Bisieccion:    " ,creciente ( 0 , 100 ))
print ("Triseccion:    " ,tri ( 0 , 100 ))
print ("Cuatriseccion: " ,cua ( 0 , 100 ))
print ("General:       " , general(0 , 100 , 10))
