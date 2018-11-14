#ejemplos para la funcion del metodo secante

f <- function(x){
  return (x*x -1)
}


g <- function(x){
  return (sin(x))
}

h <- function(x){
  return (x^3 - 4*x^2 + 5*x +88 )
}


secante(f , 0 , 2)

secante(g , 0.6 , 50)

#utilizando el paraetro opcional de error
secante(h , -5 , 6 , 0.0000001)

###############################################
#ejemplos para la funcion del metodo biseccion


#existe mas de una raiz en ese intervalo
bisec(f , -2 , 2)

#no existe niguna raiz en ese intervalo
bisec(f , -200 , -100)

#utilizando el parametro opcional de error
bisec( g , 0.5 , 5 , 0.000001)

bisec(h , -5 , 6)