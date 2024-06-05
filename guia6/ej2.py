import numpy as np
import random


# A)
def f(x: float) -> float:
    """
    Calcula el valor de la función f(x) = exp(x) / sqrt(2 * x).

    Parámetros:
    - x (float): El valor de entrada para la función.

    Retorna:
    - float: El valor de la función evaluada en x.
    """
    return np.exp(x) / np.sqrt(2 * x)


def media_muestral(g, d: float) -> tuple:
    """
    Estima la media y la varianza muestral de una función dada mediante muestreo aleatorio.

    Parámetros:
    - g (function): La función de la cual se estimará la media y la varianza muestral.
    - d (float): La precisión deseada para la media muestral.

    Retorna:
    - tuple: Una tupla que contiene el número de muestras, la media muestral
             y la varianza muestral de la función proporcionada.
    """
    u = random.random()
    media = g(u)
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        x = g(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, scuad


def test(d: float):
    """
    Realiza un test de montecarlo para estimar la integral de la función f(x)
    y compara el resultado con el valor exacto de la integral.

    Parámetros:
    - d (float): La precisión deseada para la media muestral.
    """
    _, media, _ = media_muestral(f, d)
    print(f"El valor exacto de la integral es {2.0685}")
    print(f"El valor de la simulacion de la integral es {media}")


# test(d=0.01)

# B)


def f2(x: float) -> float:
    t = (1 / x - 1) ** 2
    return (t * np.exp(-t)) / (x**2)


def test2(d: float):
    """
    Realiza un test de montecarlo para estimar la integral de la función f(x)
    y compara el resultado con el valor exacto de la integral.

    Parámetros:
    - d (float): La precisión deseada para la media muestral.
    """
    _, media, _ = media_muestral(f2, d)
    media = media * 2
    print(f"El valor exacto de la integral es {0.886227}")
    print(f"El valor de la simulacion de la integral es {media}")


test2(d=0.01)
