import random
import numpy as np
import math


# I)
def trnasformada_inversa_pareto(*, a: float) -> float:
    """
    Genera una variable aleatoria continua utilizando el método de la transformada inversa para la distribución de Pareto.

    Args:
        a (float): Parámetro de forma de la distribución de Pareto.

    Returns:
        float: El valor de la variable aleatoria generada.
    """
    u = random.random()
    return (1 / u) ** (1 / a)


def test(*, n: int, a: float):
    """
    Compara el valor esperado teorico con el obtenido por la simulacion.

    Args:
        n (int): El número de muestras a generar para la estimación.
        a (float): Parámetro de forma de la distribución de Pareto.

    Prints:
        Imprime la esperanza teórica y la esperanza estimada con el número de muestras dado.
    """
    prom = 0.0
    for _ in range(n):
        prom += trnasformada_inversa_pareto(a=2)
    prom = prom / n
    print(f"La esperanza teorica es: {a/(a-1)}")
    print(f"La esperanza con n = {n} es: {prom}")


test(n=1000, a=2)

# II)


def Erlang(*, x: float, u: float, k: int) -> float:
    """
    Calcula el valor de la función de densidad de probabilidad de la distribución Erlang en un punto específico.

    Args:
        x (float): Punto en el que se desea evaluar la función de densidad de probabilidad.
        u (float): Parámetro de la distribución Erlang.
        k (int): Parámetro de forma de la distribución Erlang.

    Returns:
        float: El valor de la función de densidad de probabilidad en el punto dado.
    """
    t1 = x ** (k - 1) * np.exp(-x / u)
    t2 = math.factorial(k - 1) * (u**k)
    return t1 / t2


def GeneraExponencial(*, lamda: float) -> float:
    """
    Genera una variable aleatoria exponencial utilizando el método de la transformada inversa.

    Args:
        lamda (float): Parámetro de tasa de la distribución exponencial.

    Returns:
        float: El valor de la variable aleatoria generada.
    """
    U = 1 - random.random()
    return -np.log(U) / lamda


def generaNexponenciales(*, n: int, lamda: float) -> float:
    """
    Genera la suma de n variables aleatorias exponenciales.

    Args:
        n (int): El número de variables exponenciales a generar.
        lamda (float): Parámetro de tasa de la distribución exponencial.

    Returns:
        float: La suma de las variables aleatorias generadas.
    """
    sum = 0
    for _ in range(n):
        sum += GeneraExponencial(lamda=lamda)
    return sum


def AyR(*, n: int, lamda: float) -> float:
    """
    Genera una variable aleatoria Erlang sumando n variables aleatorias exponenciales.

    Args:
        n (int): El número de variables exponenciales a sumar.
        lamda (float): Parámetro de tasa de la distribución exponencial.

    Returns:
        float: El valor de la variable aleatoria Erlang generada.

    en la funcion de erlang el k es el n
    """
    return generaNexponenciales(n=n, lamda=lamda)


def test2(*, n: int, k: int, lamda: float):
    """
    Compara el valor esperado teorico con el obtenido por la simulacion.

    Args:
        n (int): El número de muestras a generar para la estimación.
        k (int): Parámetro de forma de la distribución Erlang.
        lamda (float): Parámetro de tasa de la distribución exponencial.

    Prints:
        Imprime la esperanza teórica y la esperanza estimada con el número de muestras dado.
    """
    sum = 0
    for _ in range(n):
        sum += AyR(n=k, lamda=lamda)
    print(f"La esperanza teorica es {k/lamda}")
    print(f"La esperanza con {n} iteraciones es: {sum/n}")


# test2(n=1000, k=2, lamda=1)
