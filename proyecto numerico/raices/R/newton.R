sec <- function(f , x1 , x2){
  res <- ((x2-x1) / (f(x2)-f(x1)))

  return ( res )

}

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


