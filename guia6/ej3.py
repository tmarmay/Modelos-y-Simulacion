import random
import numpy as np


def f(x: float) -> float:
    """
    Calcula el valor de la función f(x).

    Parámetros:
    - x (float): El valor de entrada para la función.

    Retorna:
    - float: El valor de la función evaluada en x.
    """
    t = (3 + ((1 / x - 1) ** 4)) * (x**2)
    return 1 / t


def f2(x: float) -> float:
    """
    Calcula el valor de la función f2(x).

    Parámetros:
    - x (float): El valor de entrada para la función.

    Retorna:
    - float: El valor de la función evaluada en x.
    """
    t = x * np.pi + np.pi
    return (np.sin(t) * np.pi) / t


def Media_Muestral_X(g, z_alfa_2: float, L: float) -> float:
    """
    Estima la media muestral de una función dada mediante muestreo aleatorio.

    Parámetros:
    - g (function): La función de la cual se estimará la media muestral.
    - z_alfa_2 (float): El valor crítico z para un nivel de confianza del 95%.
    - L (float): La longitud del intervalo de confianza deseado.

    Retorna:
    - tuple: Una tupla que contiene el número de iteraciones realizadas y la media muestral estimada.
    """
    d = L / (2 * z_alfa_2)
    media = g(random.random())
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        x = g(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media


def test(z_alfa_2: float, L: float):
    """
    Realiza un test de montecarlo para estimar la integral de la función f(x)
    y compara el resultado con el valor exacto de la integral.

    Parámetros:
    - z_alfa_2 (float): El valor crítico z para un nivel de confianza del 95%.
    - L (float): La longitud del intervalo de confianza deseado.
    """
    n, media = Media_Muestral_X(f, z_alfa_2, L)
    media = media * 3
    print(f"El valor exacto de la integral es {1.4618}")
    print(
        f"El valor de la simulacion de la integral es {media} luego de {n} iteraciones"
    )


# test(z_alfa_2=1.96, L=0.001)


def test2(z_alfa_2: float, L: float):
    """
    Realiza un test de montecarlo para estimar la integral de la función f2(x)
    y compara el resultado con el valor exacto de la integral.

    Parámetros:
    - z_alfa_2 (float): El valor crítico z para un nivel de confianza del 95%.
    - L (float): La longitud del intervalo de confianza deseado.
    """
    n, media = Media_Muestral_X(f2, z_alfa_2, L)
    media = media
    print(f"El valor exacto de la integral es {-0.433785}")
    print(
        f"El valor de la simulacion de la integral es {media} luego de {n} iteraciones"
    )


test2(z_alfa_2=1.96, L=0.001)
