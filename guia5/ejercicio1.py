import random
import math
from matplotlib import pyplot as plt
import numpy as np


# A)
def trasnf_inversa_continua() -> float:
    """
    Genera una variable aleatoria continua utilizando el método de transformación inversa.

    Returns:
        float: El valor de la variable aleatoria generada.
    """
    u = random.random()
    if u < 0.25:
        return 2 * math.sqrt(u) + 2
    else:
        return 6 - math.sqrt(-12 * u + 12)


def testA(*, n: int):
    """
    Compara el valor esperado teorico con el obtenido por la simulacion.

    Args:
        n (int): El número de muestras a generar para la estimación.

    Prints:
        Imprime la esperanza teórica y la esperanza estimada con el número de muestras dado.
    """
    sum = 0
    for _ in range(n):
        sum += trasnf_inversa_continua()
    print(f"La esperanza teorica es {7/4}")
    print(f"La esperanza con n = {n} es: {sum/n}")


# testA(n = 1000)


# B)
def tib() -> float:
    """
    Genera una variable aleatoria continua utilizando el método de la transformada inversa.

    Returns:
        float: El valor de la variable aleatoria generada.
    """
    u = random.random()
    if u < 0.25:
        return math.log(16 * u) / 4
    else:
        return 4 * u


def test2(*, n: float):
    """
    Compara el valor esperado teorico con el obtenido por la simulacion.

    Args:
        n (float): El número de muestras a generar para la estimación.

    Prints:
        Imprime la esperanza teórica y la esperanza estimada con el número de muestras dado.
    """
    sum = 0
    for _ in range(n):
        sum += tib()
    print(f"La esperanza teorica es {223/128}")
    print(f"La esperanza con n = {n} es: {sum/n}")


test2(n=1000)
