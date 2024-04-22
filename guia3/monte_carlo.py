import random 
from typing import Callable

def MonteCarlo(g: Callable[[int], int], Nsim: int):
    """
    Realiza una estimacion numorica de la integral de una funcion g
    utilizando el motodo de Monte Carlo.

    Parometros:
    - g: funcion de una variable que se desea integrar.
    - Nsim: numero de simulaciones a realizar.

    Retorna:
    - Aproximacion de la integral de g sobre el intervalo [0, 1].

    Ejemplo de uso:
    >>> def f(x):
    ...     return x ** 2
    >>> MonteCarlo(f, 10000)
    0.33346
    """
    integral = 0
    for _ in range(Nsim):
        integral += g(random.random())
    return integral/Nsim


def MonteCarlo2Dim(g, Nsim: int):
    """
    Realiza una estimacion numerica de la integral doble,
    utilizando el metodo de Monte Carlo.

    Parametros:
    - g: funcion de dos variables que se desea integrar.
    - Nsim: numero de simulaciones a realizar.

    Retorna:
    - Aproximacion de la integral de g sobre el cuadrado unitario [0, 1]x[0, 1].

    Ejemplo de uso:
    >>> def f(x, y):
    ...     return x**2 + y**2
    >>> MonteCarlo2Dim(f, 10000)
    0.66679
    """
    integral = 0
    for _ in range(Nsim):
        x = random.random()
        y = random.random()
        integral += g(x,y)
    return integral/Nsim