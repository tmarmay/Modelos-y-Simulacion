import random
import math
import numpy as np


def GeneraTI() -> float:
    """
    Genera un valor aleatorio de acuerdo con la probabilidad definida
    por los rangos especificados utilizando el metodo de trasnformada a la inversa.

    Returns:
        float: El valor generado.
    """
    u = random.random()
    return np.exp(u)


def GeneraXAyR() -> float:
    """
    Genera un valor aleatorio utilizando el método de aceptación y rechazo.
    Generado el Y con distribucion uniforme.

    Returns:
        float: El valor generado.
    """
    while True:
        y = (math.e - 1) * random.random() + 1
        u = random.random()
        if u < 1 / y:
            return y


def test(*, k: int):
    """
    Compara el valor esperado teorico con el obtenido por la simulacion.

    Args:
        k (int): El número de muestras a generar para la estimación.

    Prints:
        Imprime la esperanza teórica y la esperanza estimada con el número de muestras dado.
    """
    sumti, sumayr = 0, 0
    for _ in range(k):
        sumti += GeneraTI()
        sumayr += GeneraXAyR()
    print(f"La esperanza teorica es {1.71}")
    print(f"La esperanza con {k} iteraciones es para trasnformada inversa: {sumti/k}")
    print(f"La esperanza con {k} iteraciones es para rechazo: {sumayr/k}")


def test2(k: int):
    """
    Compara el P(X <= 2) teorico con el obtenido por la simulacion.

    Args:
        k (int): El número de muestras a generar para la estimación.

    Prints:
        Imprime P(X <= 2) teorico y el obtenido por la simulacionla con el número de muestras dado.
    """
    sumti, sumayr = 0, 0
    for _ in range(k):
        if GeneraTI() <= 2:
            sumti += 1

        if GeneraXAyR() <= 2:
            sumayr += 1

    print(f"P(X <= 2) teorica es {math.log(2)}")
    print(f"P(X <= 2) con {k} iteraciones para trasnformada inversa: {sumti/k}")
    print(f"P(X <= 2) con {k} iteraciones para rechazo: {sumayr/k}")


test2(k=10_000)
