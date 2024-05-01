from ejercicio5 import BinomialTI
import random
import time


def GeneraXTI() -> int:
    """
    Genera un valor aleatorio de acuerdo con la probabilidad definida
    por los rangos especificados utilizando el metodo de trasnformada a la inversa.

    Returns:
        int: El valor generado.
    """
    U = random.random()
    if 0.45 <= U < 0.8:
        return 3
    elif 0.8 <= U:
        return 4
    elif 0.1 <= U < 0.35:
        return 1
    elif 0 <= U < 0.15:
        return 0
    else:
        return 2


def GeneraXAyR(c: float, n: int, p: float, vprob: list) -> int:
    """
    Genera un valor aleatorio utilizando el método de aceptación y rechazo.
    Generado el Y con el metodo de transformada a la inversa de una binomial

    Args:
        c (float): Constante de ajuste.
        n (int): Número de ensayos para la distribución binomial.
        p (float): Probabilidad de éxito para la distribución binomial.
        vprob (list): Lista de probabilidades para cada xi.

    Returns:
        int: El valor generado.
    """
    while True:
        y = BinomialTI(n, p)
        if random.random() < vprob[y] / c:
            return y


"""
Como llamarlas
GeneraXAyR(c=0.84, n=4, p=0.45, vprob=vprob)
GeneraXTI()
"""
vprob = [0.15, 0.2, 0.1, 0.35, 0.2]


def ComparaSimulaciones(n: int):
    """
    Compara el tiempo de ejecución de GeneraXTI() y GeneraXAyR() para un número dado de iteraciones.

    Args:
        n (int): Número de iteraciones para comparar el rendimiento.
    """
    comienzo = time.time()
    for _ in range(n):
        GeneraXTI()
    final = time.time()
    print(
        f"Tiempo de ejecucion para n = {n} con metodo de transformada a la inversa: {final-comienzo}"
    )

    comienzo = time.time()
    for _ in range(n):
        GeneraXAyR(c=0.84, n=4, p=0.45, vprob=vprob)
    final = time.time()
    print(
        f"Tiempo de ejecucion para n = {n} con metodo de aceptacion y rechazo: {final-comienzo}"
    )


ComparaSimulaciones(10000)
