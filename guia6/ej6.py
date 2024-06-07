import random
import numpy as np


def estimacion_pi(nsim: int) -> float:
    """
    Estima el valor de pi utilizando el método de Monte Carlo.

    Parámetros:
    - nsim (int): Número de simulaciones.

    Retorna:
    - float: Estimación de pi.
    """
    sum = 0
    for _ in range(nsim):
        u = random.random()
        v = random.random()
        if (u**2) + (v**2) <= 1:
            sum += 1
    return 4 * (sum / nsim)


def media_muestral(g, d: float, nsim: int) -> tuple:
    """
    Calcula la media muestral de una función con precisión dada.

    Parámetros:
    - g: Función para estimar la media.
    - d (float): Precisión deseada.
    - nsim (int): Número de simulaciones.

    Retorna:
    - tuple: Número de iteraciones, media muestral, y varianza de la media.
    """
    media = g(nsim)
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        media_ant = media
        x = g(nsim)
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, scuad


def test(d: float, nsim: int):
    """
    Realiza una prueba con una precisión dada.

    Parámetros:
    - d (float): Precisión deseada.
    - nsim (int): Número de simulaciones.
    """
    n, media, scuad = media_muestral(estimacion_pi, d, nsim)
    print(f"La aproximacion de pi dio {media} en {n} iteraciones")


test(d=0.01, nsim=1000)


def Media_Muestral_X(g, z_alfa_2: float, L: float, nsim: int) -> float:
    """
    Calcula la media muestral de una función para un intervalo dado.

    Parámetros:
    - g: Función para estimar la media.
    - z_alfa_2 (float): Valor crítico para el intervalo de confianza.
    - L (float): Longitud deseada del intervalo.
    - nsim (int): Número de simulaciones.

    Retorna:
    - tuple: Número de iteraciones y media muestral.
    """
    d = L / (2 * z_alfa_2)
    media = g(nsim)
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        x = g(nsim)
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media


def test2(z_alfa_2: float, L: float, nsim: int):
    """
    Realiza una prueba para calcular la media muestral con un intervalo de confianza.

    Parámetros:
    - z_alfa_2 (float): Valor crítico para el intervalo de confianza.
    - L (float): Longitud deseada del intervalo.
    - nsim (int): Número de simulaciones.
    """
    n, media = Media_Muestral_X(estimacion_pi, z_alfa_2, L, nsim)
    media = media
    print(f"La aproximacion de pi es {media} en {n} iteraciones")


test2(z_alfa_2=1.645, L=0.1, nsim=1000)
