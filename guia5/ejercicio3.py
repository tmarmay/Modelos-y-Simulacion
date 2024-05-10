import random
import numpy as np


def composicion(fi_pi: list):
    """
    Realiza el proceso de composición para generar una v.a.

    Args:
        fi_pi (list): Una lista de tuplas donde cada tupla contiene dos elementos:
                      el primero es la probabilidad acumulada y el segundo es una función para generar una variable aleatoria.

    Returns:
        function: La función seleccionada aleatoriamente según la probabilidad acumulada usando el metodo de composicion.
    """
    fi_pi.sort(key=lambda tup: tup[0])
    u = random.random()
    i = 0
    while u > fi_pi[i][0]:
        i += 1
    fi = fi_pi[i][1]
    return fi


def GeneraExponencial(lamda: float) -> float:
    """
    Genera una variable aleatoria exponencial.

    Args:
        lamda (float): Parámetro de tasa de la distribución exponencial.

    Returns:
        float: El valor de la variable aleatoria generada.
    """
    U = 1 - random.random()
    return -np.log(U) / lamda


def test(*, n: int):
    """
    Compara el valor esperado teorico con el obtenido por la simulacion.

    Args:
        n (int): El número de muestras a generar para la estimación.

    Prints:
        Imprime la esperanza teórica y la esperanza estimada con el número de muestras dado.
    """
    sum = 0
    for _ in range(n):
        sum += composicion(
            [
                (0.5, GeneraExponencial(1 / 3)),
                (0.8, GeneraExponencial(1 / 5)),
                (1, GeneraExponencial(1 / 7)),
            ]
        )
    print(f"La esperanza teorica es {4.4}")
    print(f"La esperanza con {n} iteraciones es: {sum/n}")


test(n=1000)
