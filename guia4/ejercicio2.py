import random
import math
import time

g = lambda x, n: math.e ** (x / n)


def CalculoDePromedio(f, n, k):
    """
    Calcula el promedio ponderado de una función 'f' evaluada en 'k' números aleatorios entre 1 y 10_000,
    ponderados por un factor 'n'.

    Parámetros:
    f : función
        La función a evaluar en los números aleatorios generados.
    n : int
        El factor de ponderación para el promedio.
    k : int
        El número de veces que se evaluará la función.

    Retorna:
    float
        El promedio ponderado de las evaluaciones de la función multiplicado por 'n'.

    Ejemplo:
    >>> def cuadrado(x, n):
    ...     return x ** 2 + n
    >>> CalculoDePromedio(cuadrado, 2, 5)
    337470.0
    """
    sum = 0
    for _ in range(k):
        u = random.randrange(0, n + 1)
        sum += f(u, n)
    prmedio = sum / k
    return prmedio * n


# print(CalculoDePromedio(g, n=10_000, k=100))


def PruebaRendimiento(n):
    resultado = 0
    tiempo_inicio = time.time()
    for i in range(n):
        resultado += g(i, n)
    tiempo_final = time.time()
    print(f"Calculo de los primeros 100 numeros en la funcion g")
    print(f"            {resultado}, tiempo: {tiempo_final-tiempo_inicio}")

    tiempo_inicio = time.time()
    resultado = CalculoDePromedio(g, n, 100)
    tiempo_final = time.time()
    print(f"Calculo de los primeros 100 numeros en la funcion g con aproximacion")
    print(f"           {resultado}, tiempo: {tiempo_final-tiempo_inicio}")


PruebaRendimiento()
