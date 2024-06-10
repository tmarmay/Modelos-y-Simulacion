import scipy.stats as stats
import random


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
    """
    Genera una muestra de valores de una distribución binomial.

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
    for i in range(1, len(pi) - 1):
        sum_p -= pi[i - 1]
        nj = generar_binomial(n - sum_nj, pi[i] / sum_p)
        sum_nj += nj
        ni.append(nj)
    ni.append(n - sum_nj)
    return ni


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


def test(*, nsim: int, grados_libertad: int):
    ns = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
    ps = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
    t0 = calcular_estadistico_pearson(ni=ns, pi=ps, n=637)

    print(f"El valor teorico del p-valor es {1 - stats.chi2.cdf(t0, grados_libertad)}")
    print(
        f"El valor por simulacion del p-valor es {estimar_p_valor(nsim, t0, ps, 637)}"
    )


test(nsim=10_000, grados_libertad=9)
