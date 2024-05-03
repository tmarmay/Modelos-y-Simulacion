import random
import numpy as np
from matplotlib import pyplot as plt


def DistribucionX(j: int) -> float:
    """
    Calcula la función de distribución de probabilidad para un valor dado de 'j'.

    Parámetros:
    - j (int): Un entero mayor que 0.

    Retorna:
    float: El valor calculado de la función de distribución de probabilidad para el 'j' dado.
    """
    t1 = 0.5 ** (j + 1)
    t2 = 0.5 * (2**j - 1)
    t3 = 3**j
    return t1 + t2 / t3


def GeneraX() -> int:
    """
    Genera un entero aleatorio 'i' siguiendo una distribución de 'DistribucionX'.

    Retorna:
    int: El entero aleatorio 'i' generado.
    """
    U = random.random()
    t1, t2, t3 = 0.25, 0.5, 3.0
    i = 1
    F = t1 + t2 / t3
    while U >= F:
        i += 1
        t1 *= 0.5
        t2 *= 2
        t3 *= 3
        F += t1 + t2 / t3
    return i


def test(n: int, k: int):
    """
    Realiza una prueba generando números aleatorios y graficando su distribución.

    Parámetros:
    - n (int): El número de iteraciones para la prueba.
    - k (int): El límite superior para el intervalo del grafico.

    Retorna:
    None
    """
    xs = [x for x in range(k + 1)]
    ys = [DistribucionX(x) * n for x in range(k + 1)]

    xi = np.zeros(k + 1)
    for _ in range(n):
        z = GeneraX()
        if z <= k:
            xi[z] += 1

    plt.bar(xs, xi, label="xi generados", color="blue")
    plt.plot(xs, ys, label="Distribucion de probabiliad", color="red")
    plt.legend()
    plt.show()


test(n=1000, k=15)
