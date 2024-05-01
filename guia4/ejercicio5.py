import random
import time
import numpy as np
from matplotlib import pyplot as plt


# I)
def BinomialTI(n: int, p: float) -> int:
    """
    Genera un número aleatorio con una distribución binomial utilizando el método de la transformada inversa.

    Args:
        n (int): Número de ensayos.
        p (float): Probabilidad de éxito en cada ensayo.

    Returns:
        int: Número de éxitos en los n ensayos.
    """
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    U = random.random()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


# II)
def Binomial(n: int, p: float) -> int:
    """
    Genera un número aleatorio con una distribución binomial realizando 'n' ensayos independientes con prob p.

    Args:
        n (int): Número de ensayos.
        p (float): Probabilidad de éxito en cada ensayo.

    Returns:
        int: Número de éxitos en los n ensayos.
    """
    exito = 0
    for _ in range(n):
        if random.random() <= p:
            exito += 1
    return exito


# A)
def ComparaTimepo(n: int, p: int):
    """
    Compara el tiempo de ejecución de las funciones BinomialTI y Binomial.

    Args:
        n (int): Número de ensayos.
        p (int): Probabilidad de éxito en cada ensayo.
    """
    comienzo = time.time()
    for _ in range(10000):
        BinomialTI(n, p)
    final = time.time()
    print(f"BinomialTI tardo {final-comienzo}")

    comienzo = time.time()
    for _ in range(10000):
        Binomial(n, p)
    final = time.time()
    print(f"Binomial haciendo n ensayos tardo {final-comienzo}")


# B)
def AnalisisVariablesAleatorias(it: int, n: int, p: float):
    """
    Analiza las variables aleatorias generadas por las funciones BinomialTI y Binomial.

    Args:
        it (int): Número de iteraciones para el análisis.
        n (int): Número de ensayos.
        p (float): Probabilidad de éxito en cada ensayo.
    """
    xs = [x for x in range(n + 1)]
    ya, yb = np.zeros(n + 1), np.zeros(n + 1)

    for _ in range(it):
        k, j = BinomialTI(n, p), Binomial(n, p)
        ya[k] += 1
        yb[j] += 1

    plt.plot(xs, ya, color="red", label="Metodo transformada inversa")
    plt.plot(xs, yb, color="green", label="Simulando n ensayos")
    plt.legend()
    plt.show()
