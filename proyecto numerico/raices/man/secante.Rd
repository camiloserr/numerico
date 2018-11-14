\name{secante}
\alias{secante}
\title{
Metodo de la secante
}
\description{
 la funciÃ³n toma dos puntos (x0 y x1) y calcula la secante entre ellos, el siguiente valor de x serÃ¡ el punto donde esa recta secante corta el eje X, esto lo hace iterativamente hasta que llegue a un valor aproximado a la raÃ�z.
}
\usage{
secante(f, ant, xi, error)
}
\arguments{
  \item{f}{
 f es la funciÃ³n a la que se le encontrarÃ¡ la RaÃ�z, debe estar previamente definida como se muestra en el ejemplo.
}
  \item{ant}{
es el valor inicial de la secuencia x0
}
  \item{xi}{
 es el segundo valor de la secuencia x1
}
  \item{error}{
 es el valor del error con el que se quiere aproximar la raÃ�z de la funciÃ³n
}
}
\details{
   Puede no recibir el parÃ¡metro 4 cuatro. Si no se pone este parÃ¡metro, se usarÃ¡ el error quemado en el cÃ³digo
}
\value{
 Retorna el valor x(n+1) que se aproxima a la raÃ�z. Si no encontro una raÃ�z retornarÃ¡ infinito.
}
\references{

}
\author{
 Daniel Mendoza y Camilo Serrano
}
\note{
 Los puntos iniciales de la funciÃ³n debrían ser considerablemente cercanos y no ser valores en X que representen un punto crÃ�tico o cuya secante sea tenga una pendiente cercana o igual a 0
}



\seealso{

}
\examples{
f <- function(x)
{
  return(sin(x));
}
f <- function(x)
{
  return(sin(x));
}
secante(f , 0.5 , 1.5)
secante(f , 1 , 1.5, 0.00001)



## The function is currently defined as
secante <- function(f , ant , xi, epsilon){
  if(missing(epsilon)){
    epsilon = 0.0001
  }
  it = 0;

  #h <- f(xi) * sec(f ,ant , xi);

  while(it < 500 ){
    E = abs(xi - ant)/abs(xi);
    h <- f(xi) * sec(f , ant , xi);
    ant <- xi;
    xi <- xi - h;
    #print(sec(f , xi , ant));

    if( abs (f(xi) ) < epsilon){
      cat("error: ", E , "\n");
      return (xi);
    }
    it <- it+1;

  }
  print("no converge, seleccione otros dos puntos que no se acerquen a un punto crítico");
  return (Inf);

}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{ ~kwd1 }% use one of  RShowDoc("KEYWORDS")
\keyword{ ~kwd2 }% _ONLY ONE_ keyword per line
