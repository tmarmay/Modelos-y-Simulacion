import random


def GeneraExp(*, lamda: float):
    pass


def SimulacionReclamos(*, p: float, n: int, lamda: float, GeneraExp):
    """
    Realiza una simulación de reclamos.

    Parameters:
        p (float): Probabilidad de que ocurra un reclamo.
        n (int): Número clientes, solo pueden hacer un reclamo cada uno.
        lamda (float): Parámetro lambda de la distribución exponencial.
        GeneraExp (función): Función para generar números aleatorios con distribución exponencial.

    Returns:
        float: La suma total de reclamos en las simulaciones.
    """
    sum = 0
    for _ in range(n):
        u = random()
        if u < p:
            y = GeneraExp(lamda)
            sum += y
    return sum


def Prob(*, n: int, k: int):
    """
    Calcula la probabilidad de que el número de reclamos sea menor que k.
    P(X <= k) donde X: Suma de los recalmos (en $)

    Parameters:
        n (int): Número de simulaciones a realizar.
        k (int): Número límite de reclamos.

    Returns:
        float: La probabilidad calculada.
    """
    j = 0
    for _ in range(n):
        if SimulacionReclamos(p=0.05, n=1000, lamda=1 / 800, GeneraExp=GeneraExp) < k:
            j += 1
    return j / n


Prob(n=10_000, k=50_000)
