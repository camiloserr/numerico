
bisec <- function(f , a , b , epsilon){
  if(missing(epsilon)){
    epsilon = 0.0001
  }

  c<-(a+b)/2;
  while(f(c)!=0 && b-a > epsilon)
  {

    if( (f(a) * f(b)) > 0){
      stop('Existe mas de una raiz o no existe ninguna en este intervalo')
    }

    if(f(c) * f(a) <0)
    {
      b<-c
    }
    else
    {
      a<-c
    }

    c<-(a+b)/2;

  }

  if(abs(f(c) ) < epsilon ||  b-a < epsilon){
    return(c)
  }
  else{
    stop('no hay una solucion en ese intervalo')
  }
}


