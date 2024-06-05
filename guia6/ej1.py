import numpy as np
import random


def GeneraNormal(mu: float, sigma: float) -> float:
    """
    Genera un número aleatorio de una distribución normal.

    Parámetros:
    - mu (float): La media de la distribución normal.
    - sigma (float): La desviación estándar de la distribución normal.

    Retorna:
    - float: Un número aleatorio generado de la distribución normal especificada.
    """
    nv_magicconst = 4 * np.exp(-0.5) / np.sqrt(2.0)
    while True:
        u1 = random.random()
        u2 = 1 - random.random()
        z = nv_magicconst * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -np.log(u2):
            break
    return mu + z * sigma


def media_muestral(mu: float, sigma: float, d: float) -> tuple:
    """
    Calcula la media y la varianza muestral dados los parámetros de la distribución.

    Parámetros:
    - mu (float): La media de la distribución normal.
    - sigma (float): La desviación estándar de la distribución normal.
    - d (float): La precisión deseada para la media muestral.

    Retorna:
    - tuple: Una tupla que contiene el número de muestras, la media muestral y la varianza muestral.
    """
    media = GeneraNormal(mu, sigma)
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        x = GeneraNormal(mu, sigma)
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, scuad


def test1(nsim: int):
    """
    Realiza un test de montecarlo para calcular la media y la varianza muestral.

    Parámetros:
    - nsim (int): El número de simulaciones a realizar.
    """
    n, media, scuad = 0, 0, 0
    for _ in range(nsim):
        a, b, c = media_muestral(mu=0, sigma=1, d=0.1)
        n += a
        media += b
        scuad += c
    n = n / nsim
    media = media / nsim
    scuad = scuad / nsim

    print(f"La cantidad de datos generados es de {n}")
    print(f"La media muestral de los datos generados es {media}")
    print(f"La varianza muestral de los datos generados es {scuad}")
