import numpy as np
from scipy.stats import uniform


def calcular_estadistico_km(ys: list, n: int, F) -> float:
    """
    Calcula el estadístico D de Kolmogorov-Smirnov para una muestra dada y una función de distribución.

    Args:
        ys (list): Lista de valores de la muestra.
        n (int): Tamaño de la muestra.
        F (callable): Función de distribución acumulada (CDF) a comparar.

    Returns:
        float: El valor del estadístico D de Kolmogorov-Smirnov.
    """
    ys.sort()
    d = 0
    for i in range(n):
        f_yi = F(ys[i])
        d = max(d, ((i + 1) / n) - f_yi, f_yi - (i / n))
    return d


def estimar_p_valor_ks(nsim: int, dvalor: float, n: int):
    """
    Estima el p-valor para la prueba de Kolmogorov-Smirnov utilizando simulaciones de Monte Carlo.

    Args:
        nsim (int): Número de simulaciones a realizar.
        dvalor (float): Valor del estadístico D observado.
        n (int): Tamaño de la muestra.

    Returns:
        float: Aproximación del p-valor.
    """
    pvalor = 0
    for _ in range(nsim):
        uniformes = np.random.uniform(low=0, high=1, size=n)
        uniformes.sort()
        dj = 0
        for j in range(n):
            uj = uniformes[j]
            dj = max(dj, ((j + 1) / n) - uj, uj - (j / n))
        if dj >= dvalor:
            pvalor += 1
    return pvalor / nsim


def test(*, nsim: int):
    """
    Realiza una prueba de Kolmogorov-Smirnov para una muestra dada y estima el p-valor.

    Args:
        nsim (int): Número de simulaciones a realizar para la estimación del p-valor.

    Prints:
        El valor del estadístico D de Kolmogorov-Smirnov y la aproximación del p-valor.
    """
    yi = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
    F = uniform.cdf  # Cumulative distribution function
    dvalor = calcular_estadistico_km(yi, len(yi), F)
    print(f"El d-valor es de: {dvalor}")
    print(f"Aproximacion del p-valor: {estimar_p_valor_ks(nsim, dvalor, len(yi))}")


test(nsim=10_000)
