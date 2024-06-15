import scipy.stats as stats
import random
import numpy as np


# EJERCICIO 3
def generar_binomial(n: int, p: float) -> int:
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


def calcular_estadistico_pearson(ni: list, pi: list, n: int) -> float:
    t0 = 0
    for i in range(len(ni)):
        t0 += ((ni[i] - n * pi[i]) ** 2) / (n * pi[i])
    return t0


def estimar_p_valor(nsim: int, t0: float, n: int, ps: list) -> float:
    pvalor = 0
    for _ in range(nsim):
        ni = generar_muestra(n, ps)
        p_estimado = calcular_p(ni)
        pi = [stats.binom.pmf(k=i, n=3, p=p_estimado, loc=0) for i in range(4)]
        T = calcular_estadistico_pearson(ni, pi, n)
        if T >= t0:
            pvalor += 1
    return pvalor / nsim

def calcular_p(ns: list) -> list:
    sum = 0 
    for i in range(len(ns)):
        sum += i * (ns[i] / 1000)
    return sum / 3

def ej3():
    ns = [490, 384, 111, 15]  # frecuencias
    p_estimado = calcular_p(ns)
    ps = [stats.binom.pmf(k=i, n=3, p=p_estimado, loc=0) for i in range(4)]
    n = 1000  # muestra
    t0 = calcular_estadistico_pearson(ns, ps, n)
    grados_libertad = 2
    print(f'El p_estimado es {p_estimado}')
    print(f'El t0 es {t0}')
    print(
        f"El valor aprox del p-valor por chi-cuadrado {1 - stats.chi2.cdf(t0, grados_libertad)}"
    )
    print(
        f"El valor por simulacion del p-valor es {estimar_p_valor(10_000, t0, n, ps)}"
    )

ej3()
# EJERCICIO 2
def calcula_s(xs: list, xbar: float, n: int) -> float:
    sum = 0
    for i in range(n):
        sum += (xs[i] - xbar) ** 2
    sum = sum / n
    return np.sqrt(sum)


def calcular_estadistico_km(ys: list, n: int, F, u: float, sigma: float) -> float:
    ys.sort()
    d = 0
    for i in range(n):
        f_yi = F(ys[i], u, sigma)
        d = max(d, ((i + 1) / n) - f_yi, f_yi - (i / n))
    return d


def estimar_p_valor_ks(nsim: int, dvalor: float, n: int):
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


def probabilidad_normal_estandar(x, mu, sigma):
    z = (x - mu) / sigma
    probabilidad = stats.norm.cdf(z)
    return probabilidad


def ej2():
    muestra = [1.628, 1.352, 1.800, 1.420, 1.594, 2.132, 1.614, 1.924, 1.692]
    n = len(muestra)
    u_estimado = sum(muestra) / n
    s = calcula_s(muestra, u_estimado, n)
    F = probabilidad_normal_estandar

    dvalor = calcular_estadistico_km(muestra, n, F, u_estimado, s)

    print(f"El d-valor es de: {dvalor}")
    print(f"Aproximacion del p-valor: {estimar_p_valor_ks(10_000, dvalor, n)}")


# ej2()

# EJERCICIO 4


def Media_Muestral_X(g, z_alfa_2: float, L: float) -> float:
    d = L / z_alfa_2
    media = g(random.random())
    scuad, n = 0, 1
    while n <= 100 or np.sqrt(scuad / n) > d:
        n += 1
        x = g(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, scuad


def Media_Muestral_n_it(g, nsim) -> float:
    media = g(random.random())
    scuad, n = 0, 1
    while n <= nsim - 1:
        n += 1
        x = g(random.random())
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, scuad


def g(y: float):
    t1 = (1 / y) - 1
    t2 = 1 + (t1**4)
    t3 = y**2
    return (t1 / t2) / t3


def ej4():
    n, media, scuad = Media_Muestral_X(g, z_alfa_2=1.96, L=0.001)
    s = np.sqrt(scuad)
    inter_i = lambda i, s, n: i - 1.96 * (s / np.sqrt(n))
    inter_d = lambda i, s, n: i + 1.96 * (s / np.sqrt(n))
    print(f"El area teorica es {0.78540}")
    print(f"El area aprox es {media} con desviacion {scuad} en {n} iteraciones")
    print(f"El intervalo es [{inter_i(media, s, n)}, {inter_d(media, s, n)}]")
    print("-- " * 4)
    for i in [1000, 5000, 7000]:
        n, media, scuad = Media_Muestral_n_it(g, i)
        s = np.sqrt(scuad)
        print(f"El area aprox es {media} con desviacion {s} en {n} iteraciones")
        print(f"El intervalo es [{inter_i(media, s, n)}, {inter_d(media, s, n)}]")
        print("-- " * 4)


# ej4()
