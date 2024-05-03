import random
import math
from functools import reduce
from matplotlib import pyplot as plt
import numpy as np

# A)
def Possion(lamda: float, i: int) -> float:
    """
    Calcula la probabilidad de que ocurran exactamente 'i' eventos en un proceso de Poisson
    con tasa 'lamda'.

    Parámetros:
    - lamda (float): Tasa del proceso de Poisson.
    - i (int): Número de eventos deseado.

    Retorna:
    float: La probabilidad de que ocurran exactamente 'i' eventos.
    """
    return (math.e**-lamda) * (lamda**i) * (1 / math.factorial(i))


def GeneraXTI(lamda: float, k: int) -> int:
    """
    Genera una variable aleatoria de Poisson utilizando el método de la transformada inversa.

    Parámetros:
    - lamda (float): Tasa del proceso de Poisson.
    - k (int): Límite superior para la generación de la variable aleatoria.

    Retorna:
    int: Valor de la variable aleatoria de Poisson generada.
    """
    U = random.random()
    c = reduce(lambda x, y: x + Possion(lamda, y), [x for x in range(k + 1)])
    i, p = 0, (math.e**-lamda) / c
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p
    return i


def vector_prob_X(lamda: float, y: int, k: int) -> float:
    """
    Calcula la probabilidad P(X = y).

    Parámetros:
    - lamda (float): Tasa del proceso de Poisson.
    - y (int): Valor de interés en la variable aleatoria de Poisson.
    - k (int): Límite superior para la generación de la variable aleatoria.

    Retorna:
    float: La probabilidad de que la variable aleatoria tome el valor 'y'.
    """
    numerador = Possion(lamda=lamda, i=y)
    denominador = reduce(lambda x, y: x + Possion(lamda, y), [x for x in range(k + 1)])
    return numerador / denominador


def GeneraXAyR(lamda: float, k: int, c: int, px) -> float:
    """
    Genera una variable aleatoria de Poisson utilizando el método de aceptación-rechazo.

    Parámetros:
    - lamda (float): Tasa del proceso de Poisson.
    - k (int): Límite superior para la generación de la variable aleatoria.
    - c (int): Constante de normalización.
    - px (function): Función de probabilidad de la variable aleatoria.

    Retorna:
    float: Valor de la variable aleatoria de Poisson generada.
    """
    while True:
        y = int(random.random() * (k + 1))
        if random.random() < px(lamda, y, k) / c:
            return y


def test(lamda: float, k: int, c: int, n: int):
    """
    Realiza pruebas comparativas entre el método de transformada inversa y el método de aceptación-rechazo.

    Parámetros:
    - lamda (float): Tasa del proceso de Poisson.
    - k (int): Límite superior para la generación de la variable aleatoria.
    - c (int): Constante de normalización.
    - n (int): Número de repeticiones de la prueba.
    """
    xs = [x for x in range(k + 1)]
    yAyR, yTI, ydistribucion = np.zeros(k + 1), np.zeros(k + 1), []

    for i in range(n):
        yTI[GeneraXTI(lamda=lamda, k=k)] += 1
        yAyR[GeneraXAyR(lamda=lamda, k=k, c=c, px=vector_prob_X)] += 1

    for i in range(k + 1):
        pi = vector_prob_X(lamda=lamda, y=i, k=k) * n
        ydistribucion.append(pi)

    plt.bar(xs, yTI, label="Metodo transformada inversa", color="blue")
    plt.bar(xs, yAyR, label="Metodo transformada aceptacion rechazo", color="green")
    plt.plot(xs, ydistribucion, label="Distribucion X desplazada", color="red")

    plt.xlabel("x")
    plt.ylabel("P(X = x)")
    plt.legend()
    plt.show()

#test(lamda=4, k=10, c=1.5, n=1000)
#test(lamda=10, k=10, c=1.5, n=1000) #B)

# B)
def comparacionProb(lamda: float, k: int, c: int, n: int, i: int):
    """
    Compara la probabilidad de que una variable aleatoria de Poisson exceda el valor 'i' utilizando
    el método de transformada inversa y el método de aceptación-rechazo.

    Parámetros:
    - lamda (float): Tasa del proceso de Poisson.
    - k (int): Límite superior para la generación de la variable aleatoria.
    - c (int): Constante de normalización.
    - n (int): Número de repeticiones de la comparación.
    - i (int): Valor para el cual se calcula la probabilidad de excedencia.

    Imprime:
    - El valor aproximado con el método de transformada inversa de P(X > i).
    - El valor aproximado con el método de aceptación-rechazo de P(X > i).
    - El valor exacto de P(X > i) calculado mediante la función de probabilidad vector_prob_X.
    """
    pi, ti, ayr = 0, 0, 0
    for _ in range(n+1):
        if GeneraXTI(lamda=lamda, k=k) > i:
            ti += 1 
        if GeneraXAyR(lamda=lamda, k=k, c=c, px=vector_prob_X) > i:
            ayr += 1
    
    print(f'El valor aprox con trasformada inversa de que P(X > {i}) es: {ti/n}')
    print(f'El valor aprox con aceptacion y rechazo de que P(X > {i}) es: {ayr/n}')
    
    for i in range(i):
        pi += vector_prob_X(lamda=lamda, y=i, k=k)
    pi = 1 - pi
    print(f'El valor exacto de que P(X > {i}) es: {pi}')

comparacionProb(lamda=10, k=10, c=1.5, n=1000, i=2)