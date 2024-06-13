import scipy.stats as stats
import random 
import numpy as np 
from matplotlib import pyplot as plt

def generar_binomial(n: int, p: float) -> int:
    """
    Genera un valor de una distribución binomial usando el método de la transformada inversa.

    Args:
        n (int): Número de ensayos.
        p (float): Probabilidad de éxito en cada ensayo.

    Returns:
        int: Número de éxitos en `n` ensayos.
    """
    c = p / (1 - p)
    prob = (1 - p) ** n
    F, i = prob, 0
    U = random.random()
    while U >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


def generar_muestra(n: int, pi: list) -> list:
    """Genera una muestra de valores de una distribución binomial.

    Args:
        n (int): Número total de ensayos.
        pi (list): Lista de probabilidades para cada categoría. La suma de las probabilidades debe ser 1.

    Returns:
        list: Lista con los conteos de cada categoría.

    Ejemplo:
        >>> generar_muestra(100, [0.2, 0.5, 0.3])
        [20, 50, 30]
    """
    ni = []
    sum_nj, sum_p = generar_binomial(n, pi[0]), 1
    ni.append(sum_nj)
    for i in range(1, len(pi)-1):
        sum_p -= pi[i-1]
        nj = generar_binomial(n - sum_nj, pi[i] / sum_p)
        sum_nj += nj
        ni.append(nj)
    ni.append(n-sum_nj)
    return ni


def calcular_estadistico_pearson(ni: list, pi: list, n: int) -> float:
    """
    Calcula el estadístico de Pearson para una prueba de bondad de ajuste.

    Args:
        ni (list): Lista de conteos observados.
        pi (list): Lista de probabilidades esperadas.
        n (int): Número total de observaciones.

    Returns:
        float: Valor del estadístico de Pearson.
    """
    t0 = 0
    for i in range(len(ni)):
        t0 += ((ni[i] - n * pi[i]) ** 2) / (n * pi[i])
    return t0

def estimar_p_valor(nsim: int, t0: float, pi: list, n: int) -> float:
    """Estima el p-valor usando simulaciones.

    Args:
        nsim (int): Número de simulaciones.
        t0 (float): Valor observado del estadístico de prueba.
        pi (list): Lista de probabilidades esperadas.
        n (int): Número total de observaciones.

    Returns:
        float: p-valor estimado.
    """
    pvalor = 0
    for _ in range(nsim):
        ni = generar_muestra(n, pi)
        T = calcular_estadistico_pearson(ni, pi, n)
        if T >= t0:
            pvalor += 1
    return pvalor / nsim    

def calcula_proporcion(nsim: int, g) -> float:
    sum = 0 
    for _ in range(nsim):
        x, y = 4 * random.random() -2 , 2* random.random() - 1
        z = g(x, y)
        if z <= 1:
            sum += 1
    return sum / nsim

def bernulli_area(g):
    x, y = 4 * random.random() -2 , 2* random.random() - 1
    z = g(x, y)
    if z <= 1:
        return 1
    return 0

def Media_Muestral_X(g, z_alfa_2: float, L: float, nsim: int) -> float:
    d = L / (2 * z_alfa_2)
    media = 8 * bernulli_area(g)
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        x = 8 * bernulli_area(g)
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media

#RESPUESTAS
def ej1():
    ns = [120, 114, 92, 85, 34, 33, 45, 11, 5]
    ps = [0.22, 0.20, 0.19, 0.12, 0.09, 0.08, 0.07, 0.02, 0.01]
    n = sum(ns)#tamano de la muestra

    t0 = calcular_estadistico_pearson(ns, ps, n)
    grados_libertad = 8 
    print(f'El valor de t0 = {t0}')
    print(f"Aprox de p-valor usando chi-cuadrado: {1 - stats.chi2.cdf(t0, grados_libertad)}")
    print(f"Aprox de p-valor por simulacion: {estimar_p_valor(10_000, t0, ps, n)}")

def ej4b():
    g = lambda x,y: ((x/2)**2) + (y ** 2)
    resultado = calcula_proporcion(10_000, g)
    print(f'La proporcion de ptos que cae en el elipse es {resultado}')

def ej4c():
    g = lambda x,y: ((x/2)**2) + (y ** 2)
    n, media = Media_Muestral_X(g, 1.96, 0.1, 10_000)
    print(f'{media}')


ej4c()