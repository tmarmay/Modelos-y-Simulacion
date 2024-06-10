import scipy.stats as stats
import numpy as np


def estimar_p_binomial(m: list, n: int) -> float:
    muestra = np.array(m)
    return np.average(muestra) / n


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


def test(*, grados_libertad: int, n: int):
    muestra = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
    p_estimado = estimar_p_binomial(muestra, n)
    tamano_muestra = len(muestra)

    frecuencias = [0, 1, 2, 4, 1, 1, 2, 5, 2]
    prob = [stats.binom.pmf(k=x, n=n, p=p_estimado, loc=0) for x in range(10)]
    t0 = calcular_estadistico_pearson(frecuencias, prob, tamano_muestra)

    print(f"El valor teorico del p-valor es {1 - stats.chi2.cdf(t0, grados_libertad)}")


test(grados_libertad=7, n=8)
