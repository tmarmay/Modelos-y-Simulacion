import random
import numpy as np
import time


def SumaUniformes() -> float:
    """
    Genera una variable aleatoria siguiendo la suma de dos distribuciones uniformes.

    Returns:
        float: La variable aleatoria generada.
    """
    x1 = random.random()
    x2 = random.random()
    return x1 + x2


def TI() -> float:
    """
    Genera una variable aleatoria utilizando el método de Transformada Inversa.

    Returns:
        float: La variable aleatoria generada.
    """
    u = random.random()
    if u < 0.5:
        return np.sqrt(2 * u)
    else:
        return 2 - np.sqrt(2 - 2 * u)


def AyR() -> float:
    """
    Genera una variable aleatoria utilizando el método de Aceptación-Rechazo.

    Returns:
        float: La variable aleatoria generada.
    """
    u = 2 * random.random()
    return u


def test(*, k: int):
    """
    Realiza una simulación para estimar los valores esperados para diferentes variables aleatorias.

    Args:
        k (int): El número de iteraciones para la simulación.
    """
    su, ti, ayr = 0, 0, 0
    for _ in range(k):
        su += SumaUniformes()
        ti += TI()
        ayr += AyR()
    print(f"La esperanza teorica es {1}")
    print(f"La esperanza con {k} iteraciones es para suma de unifromes: {su/k}")
    print(f"La esperanza con {k} iteraciones es para trasnformada inversa: {ti/k}")
    print(f"La esperanza con {k} iteraciones es para rechazo: {ayr/k}")


def test2(*, k: int):
    """
    Realiza una simulación para estimar las probabilidades de exceder un cierto valor para diferentes variables aleatorias.

    Args:
        k (int): El número de iteraciones para la simulación.
    """
    su, ti, ayr = 0, 0, 0
    for _ in range(k):
        if SumaUniformes() > 1.5:
            su += 1
        if TI() > 1.5:
            ti += 1
        if AyR() > 1.5:
            ayr += 1
    print(f"P(X > 1.5) teorica es {0.125}")
    print(f"P(X > 1.5) con {k} iteraciones para suma de uniformes: {su/k}")
    print(f"P(X > 1.5) con {k} iteraciones para trasnformada inversa: {ti/k}")
    print(f"P(X > 1.5) con {k} iteraciones para rechazo: {ayr/k}")
    """
    Aparentemente el metodo de rechazo no funciona bien para este caso, devido a que no tiene la misma distribucion de prob.
    Para mejor compresion hacer los calculos u < p(y) / (c * q(y)) => u < 1 => vale siempre (c = 2).
    """


test2(k=10_000)
