import numpy as np
import matplotlib.pyplot as plt
from typing import List, Callable


def generar_intervalo(a: float, b: float) -> np.ndarray:
    """
    Genera un intervalo de numeros equiespaciados entre dos valores dados.

    Parametros:
    a (int): El valor inicial del intervalo.
    b (int): El valor final del intervalo.

    Retorna:
    np.ndarray: Un arreglo de numpy que contiene numeros equiespaciados entre 'a' y 'b'.
    """
    return np.linspace(start=a, stop=b, num=50)


def generar_imagen(f: Callable[[float], float], xs: List[float]) -> List[float]:
    """
    Genera una lista de valores de funcion para una lista de valores de entrada.

    Parametros:
    f (Callable[[float], float]): La funcion para evaluar en cada valor de 'xs'.
    xs (List[float]): Una lista de valores de entrada para 'f'.

    Retorna:
    List[float]: Una lista de valores resultantes despues de aplicar 'f' a cada elemento de 'xs'.
    """
    return [f(x) for x in xs]


def graficar(xs: List[float], ys: List[float]) -> None:
    """
    Grafica una funcion dada por una lista de valores x y sus correspondientes valores y.

    Parametros:
    xs (List[float]): Una lista de valores x.
    ys (List[float]): Una lista de valores y correspondientes a los valores x.

    Retorna:
    None
    """
    plt.plot(xs, ys)
    plt.show()
