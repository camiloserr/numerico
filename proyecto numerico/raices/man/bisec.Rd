\name{bisec}
\alias{bisec}

\title{
Metodo de biseccion
}
\description{
Encuentra la solucion de f = 0 en el rango [a , b].
}
\usage{
bisec(f, a, b, epsilon)
}

\arguments{
  \item{f}{
Funcion cuya solucion se quiere encontrar.
}
  \item{a}{
Limite inferior del rango en el que e busca la solucion.
}
  \item{b}{
Limite superior del rango en el que e busca la solucion.
}
  \item{epsilon}{
Error de truncamiento que se va a utilizar (default = 1e-04).
}
}
\details{
Si existe mas de una raiz en el intervalo [a, b], no garantiza una respuesta.
Si la solucion es unica en el intervalo [a, b], garantiza una respuesta.
}
\value{
Retorna el valor de x siendo f(x) = 0 en el intervalo [a, b] o error en caso de no encontrar una solucion.
}
\references{

}
\author{
Daniel Medoza
Camilo Serrano
}
\note{
Si no hay una única raíz en el intervalo, el método dará error.
}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{

}
\examples{

h <- function(x){
  return (x^3 - 4*x^2 + 5*x +88 )
}


g <- function(x){
  return (sin(x))
}
bisec( g , 0.5 , 5 , 0.000001)

bisec(h , -5 , 6)



## The function is currently defined as
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
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{ ~kwd1 }% use one of  RShowDoc("KEYWORDS")
\keyword{ ~kwd2 }% _ONLY ONE_ keyword per line
