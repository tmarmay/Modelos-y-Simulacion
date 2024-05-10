import random
import numpy as np


def GeneraExponencial(lamda: float) -> float:
    """
    Genera una variable aleatoria exponencial.

    Args:
        lamda (float): Parámetro de tasa de la distribución exponencial.

    Returns:
        float: El valor de la variable aleatoria generada.
    """
    U = 1 - random.random()
    return -np.log(U) / lamda


def maxFi():
    """
    Calcula el máximo de tres variables aleatorias exponenciales generadas con diferentes tasas.

    Returns:
        float: El máximo valor entre las tres variables aleatorias generadas.
    """
    e1 = GeneraExponencial(1)
    e2 = GeneraExponencial(2)
    e3 = GeneraExponencial(3)
    return max(e1, e2, e3)


def minFi():
    """
    Calcula el mínimo de tres variables aleatorias exponenciales generadas con diferentes tasas.

    Returns:
        float: El mínimo valor entre las tres variables aleatorias generadas.
    """
    e1 = GeneraExponencial(1)
    e2 = GeneraExponencial(2)
    e3 = GeneraExponencial(3)
    return min(e1, e2, e3)


def test(*, n: int):
    """
    Realiza pruebas para generar y calcular el máximo y mínimo de tres variables aleatorias exponenciales.

    Args:
        n (int): El número de pruebas a realizar.

    Prints:
        Imprime los resultados de las pruebas.
    """
    for _ in range(n):
        print(f"FM = {maxFi()}")
        print(f"Fm = {minFi()}")
        print("----" * 4)


test(n=10)
