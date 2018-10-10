from turtle import *
import time

def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)
    right(120)
    snowflake(lengthSide, levels-1)
    left(60)
    snowflake(lengthSide, levels-1)


def main():
    speed(0)
    length = float(input("Tamaño inicial del triángulo: "))
    itera = float(input("Número de iteraciones: "))
    ncaras = 3 * 4**itera
    tcara = length/3**itera

    perimetro = ncaras*tcara

    penup()

    backward(length/2.0)

    pendown()
    print("Perimetro = ", perimetro)
    for i in range(3):
        snowflake(length, itera)
        right(12000)

    time.sleep(10)

main()