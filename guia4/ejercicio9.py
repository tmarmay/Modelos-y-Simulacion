import random
import math
import numpy as np
from matplotlib import pyplot as plt

"""
Si la variable aleatoria discreta X se usa para modelar el número 
total de intentos hasta obtener el primer éxito en una sucesión de
ensayos independientes Bernoulli en donde en cada uno de ellos la 
probabilidad de éxito es p
"""


def Geometrica(p: float, x: int) -> float:
    """
    Calcula la probabilidad de que ocurran exactamente 'x' ensayos independientes
    hasta obtener el primer éxito en una distribución geométrica.

    Parámetros:
    - p (float): Probabilidad de éxito en un ensayo independiente.
    - x (int): Número de ensayos independientes hasta el primer éxito.

    Retorna:
    float: La probabilidad de que ocurran exactamente 'x' ensayos independientes hasta el primer éxito.
    """
    return p * ((1 - p) ** (x - 1))


# A)
def GeneraGeometricaI(p: float) -> int:
    """
    Genera una variable aleatoria geométrica utilizando el método de la inversa de la función acumulada.

    Parámetros:
    - p (float): Probabilidad de éxito en un ensayo independiente.

    Retorna:
    int: Valor de la variable aleatoria geométrica generada.
    """
    U = random.random()
    return int(math.log(1 - U) / math.log(1 - p)) + 1


# B)
def GeneraGeometricaII(p: float) -> int:
    """
    Genera una variable aleatoria geométrica utilizando el método de la serie de ensayos independientes.

    Parámetros:
    - p (float): Probabilidad de éxito en un ensayo independiente.

    Retorna:
    int: Valor de la variable aleatoria geométrica generada.
    """
    i = 1
    while True:
        U = random.random()
        if U < p:
            return i
        i += 1


def test(n: int, p: float, k: int):
    """
    Realiza pruebas comparativas entre el método de la transformada inversa y la simulación de ensayos
    con probabilidad de éxito 'p' para generar variables aleatorias geométricas.

    Parámetros:
    - n (int): Número de repeticiones de la prueba.
    - p (float): Probabilidad de éxito en un ensayo independiente.
    - k (int): Límite superior para la generación de la variable aleatoria geométrica.

    Imprime:
    - Un gráfico comparativo entre la distribución geométrica teórica, la generada con el método de la
      transformada inversa y la generada simulando ensayos con probabilidad de éxito 'p'.
    """
    xs = [x for x in range(k + 1)]
    ys = [Geometrica(p, x) * n for x in range(k + 1)]

    yI, yII = np.zeros(k + 1), np.zeros(k + 1)
    for _ in range(n):
        l, t = GeneraGeometricaI(p), GeneraGeometricaII(p)
        if l < k:
            yI[l] += 1
        if t < k:
            yII[t] += 1

    plt.bar(xs, yI, label="Metodo transformada inversa")
    plt.bar(xs, yII, label="Simulando ensayos con probabilidad de éxito p")
    plt.plot(xs, ys, label="Distribucion geometrica")

    plt.legend()
    plt.show()


# test(n=1000, p=0.2, k=10)


# C)
def Comparacion(n: int, p: float):
    """
    Compara el valor teórico esperado y el promedio de valores obtenidos utilizando el método de la transformada inversa
    y la simulación de ensayos para generar variables aleatorias geométricas.

    Parámetros:
    - n (int): Número de repeticiones de la comparación.
    - p (float): Probabilidad de éxito en un ensayo independiente.

    Imprime:
    - El valor teórico esperado de la variable aleatoria geométrica (1/p).
    - El promedio de valores obtenidos por el método de la transformada inversa.
    - El promedio de valores obtenidos por el método de simulación de ensayos.
    """
    i, ii = 0, 0
    for _ in range(n):
        i += GeneraGeometricaI(p)
        ii += GeneraGeometricaII(p)
    print(f"Para n = {n}")
    print(f"    Valor teorico esperado = 1/p: {1/p}")
    print(
        f"    Promedio de valores obtenidos por metodo de transformada inversa: {i/n}"
    )
    print(f"    Promedio de valores obtenidos por metodo simulando ensayos: {ii/n}")


Comparacion(n=10000, p=0.8)
print("---- " * 5)
Comparacion(n=10000, p=0.2)
