import random
import math


def eventosPoisson(*, lamda: float, T: float):
    """
    Genera eventos de un proceso de Poisson con tasa lamda hasta un tiempo T.

    Parámetros:
        lamda (float): Tasa del proceso de Poisson.
        T (float): Tiempo máximo hasta el cual se generarán los eventos.

    Retorna:
        tupla: Un tupla con dos elementos:
            - El número total de eventos generados (nt).
            - Una lista con los tiempos de ocurrencia de cada evento.
    """
    t = 0
    nt = 0
    eventos = []
    while t < T:
        u = 1 - random.random()
        t += -math.log(u) / lamda
        if t <= T:
            nt += 1
            eventos.append(t)
    return nt, eventos


def eventosPoissonColectivos(*, lamda: float, T: float):
    """
    Genera eventos de un proceso de Poisson con tasa lambda hasta un tiempo T,
    simulando la llegada de autobuses de aficionados a un encuentro deportivo.

    Parámetros:
        lamda (float): Tasa del proceso de Poisson.
        T (float): Tiempo máximo hasta el cual se generarán los eventos.

    Retorna:
        tuple: Un tuple con tres elementos:
            - El número total de eventos generados (nt).
            - Una lista con los tiempos de ocurrencia de cada evento.
            - El total de personas que llegaron en los autobuses.
    """
    t, nt, eventos = 0, 0, []
    gente = 0
    while t < T:
        u = 1 - random.random()
        t += -math.log(u) / lamda
        if t <= T:
            nt += 1
            gente += int(20 * random.random()) + 20
            eventos.append(t)
    return nt, eventos, gente


def simulacionColectivos(lamda: float, T: float):
    """
    Simula la llegada de aficionados al encuentro deportivo en el instante t = 1 hora
    utilizando un proceso de Poisson para la llegada de autobuses con capacidad aleatoria.

    Parámetros:
        lamda (float): Tasa del proceso de Poisson.
        T (float): Tiempo máximo hasta el cual se generarán los eventos.

    Retorna:
        None: No retorna un valor específico, imprime en pantalla la información
        sobre la llegada de colectivos y personas.
    """

    nt, eventos, gente = eventosPoissonColectivos(lamda=lamda, T=T)
    print(f"Llegaron {nt} colectivos con {gente} personas")


# simulacionColectivos(lamda=5,T=1)


def test(*, lamda: float, T: float, n: int):
    """
    Realiza una prueba de simulación para calcular el promedio de personas y colectivos que llegan
    a un encuentro deportivo en base a múltiples simulaciones.

    Parámetros:
        lamda (float): Tasa del proceso de Poisson para la llegada de autobuses.
        T (float): Tiempo máximo hasta el cual se generarán los eventos en cada simulación.
        n (int): Número de simulaciones a realizar.

    Imprime:
        El promedio de personas y colectivos que llegan en base a las simulaciones.
    """
    prom_gente, prom_colectivos = 0, 0
    for _ in range(n):
        sim = eventosPoissonColectivos(lamda=lamda, T=T)
        gente, colectivos = sim[2], sim[0]
        prom_gente += gente
        prom_colectivos += colectivos
    print(f"El promedio de gente que llego es de {prom_gente/n}")
    print(f"El promedio de colectivos que llego es de {prom_colectivos/n}")


test(lamda=5, T=1, n=10_000)
