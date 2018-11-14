\name{secante}
\alias{secante}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Metodo de la secante
}
\description{
 la función toma dos puntos (x0 y x1) y calcula la secante entre ellos, el siguiente valor de x será el punto donde esa recta secante corta el eje X, esto lo hace iterativamente hasta que llegue a un valor aproximado a la raíz.
}
\usage{
secante(f, ant, xi, error)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{f}{
 f es la función a la que se le encontrará la Raíz
}
  \item{ant}{
es el valor inicial de la secuencia x0
}
  \item{xi}{
 es el segundo valor de la secuencia x1
}
  \item{error}{
 es el valor del error con el que se quiere aproximar la raíz de la función
}
}
\details{
   Puede no recibir el parámetro 4 cuatro. Si no se pone este parámetro, se usará el error quemado en el código
}
\value{
%%  ~Describe the value returned
 Retorna el valor x(n+1) que se aproxima a la raíz. Si no encontro una raíz retornará infinito.
}
\references{
%% ~put references to the literature/web site here ~
}
\author{
 Daniel Mendoza y Camilo Serrano
}
\note{
 Los puntos iniciales de la función deben ser considerablemente cercanos y no ser valores en X que representen un punto crítico
}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
%% objects to See Also as \code{\link{help}}, ~
}
\examples{
##---- Should be DIRECTLY executable !! ----
##-- ==>  Define data, use random,
##--	or do  help(data=index)  for the standard data sets.

## The function is currently defined as
function (f, ant, xi)
{
    it = 0
    epsilon = 1e-04
    h <- f(xi) * sec(f, ant, xi)
    while (it < 500) {
        h <- f(xi) * sec(f, ant, xi)
        ant <- xi
        xi <- xi - h
        if (abs(f(xi)) < epsilon) {
            return(xi)
        }
        it <- it + 1
    }
    print("no converge")
  }
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory.
\keyword{ ~kwd1 }% use one of  RShowDoc("KEYWORDS")
\keyword{ ~kwd2 }% __ONLY ONE__ keyword per line
