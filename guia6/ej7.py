import scipy.stats as stats
import random


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


def generar_muestra(n: int, p1: float, p2: float) -> list:
    """
    Genera una muestra de valores de una distribución Binomial.

    Args:
        n (int): Número total de ensayos.
        p1 (float): Probabilidad del primer evento.
        p2 (float): Probabilidad del segundo evento.

    Returns:
        list: Lista con los conteos de los tres posibles eventos.
    """
    n1 = generar_binomial(n, p1)
    n2 = generar_binomial(n - n1, p2 / (1 - p1))
    n3 = n - n1 - n2
    return [n1, n2, n3]


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
        ni = generar_muestra(n, pi[0], pi[1])
        T = calcular_estadistico_pearson(ni, pi, n)
        if T >= t0:
            pvalor += 1
    return pvalor / nsim


def test(*, nsim: int, grados_libertad: int, t0: float, pi: list, n: int):
    """
    Realiza una prueba de bondad de ajuste usando el estadístico de Pearson.

    Args:
        nsim (int): Número de simulaciones.
        grados_libertad (int): Grados de libertad de la distribución chi-cuadrado.
        t0 (float): Valor observado del estadístico de prueba.
        pi (list): Lista de probabilidades esperadas.
        n (int): Número total de observaciones.
    """
    print(f"El valor teorico del p-valor es {1 - stats.chi2.cdf(t0, grados_libertad)}")
    print(f"El valor por simulacion del p-valor es {estimar_p_valor(nsim, t0, pi, n)}")


test(nsim=10_000, grados_libertad=2, t0=81 / 94, pi=[0.25, 0.5, 0.25], n=564)
