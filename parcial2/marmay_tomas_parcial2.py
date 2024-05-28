import random
import math
import numpy as np


# EJERCICIO 2
def ti():
    u = random.random()
    if u < 2 / 3:
        return (1.5 * u) ** (2 / 3)
    else:
        return 3 * u - 1


def prob(n: int):
    sum = 0
    for _ in range(n):
        if ti() > 1:
            sum += 1
    print(f"P(X > 1) teorica es {1/3}")
    print(f"P(X > 1) por simulacion es {sum / n}")

# prob(n=10_000)

def test_esperanza_ti():
    sum = 0
    for _ in range(10_000):
        sum += ti()
    print(f"Esperanza teorica {9/10}")
    print(f"Esperanza simulada {sum /10_000}")


# EJERCICIO 1
def algo_x(p):
    while True:
        y = int(4 * random.random())
        u = random.random()
        if u < p[y] / (1.4 * (1 / 3)):
            return y


p = [0.13, 0.22, 0.35, 0.30]


def test_esperanza_algo_x():
    sum = 0
    for _ in range(10_000):
        sum += algo_x(p)
    print(f"Esperanza teorica {1.82}")
    print(f"Esperanza simulada {sum /10_000}")


# EJERCICIO4

def g(z, k):
    t1 = 3 * k + 1.5
    t2 = 3 * z + 1.5
    return (t1**2) + (t2 - abs((t1) ** 1.5)) ** 2


def area(n: int):
    sum = 0
    for _ in range(n):
        z = random.random()
        k = random.random()
        r = g(z, k)
        if r <= 1.5:
            sum += 1
    print(sum / n)


#area(n=10_000)


# EJERCICIO 3
def Possion_adelgazamiento_mejorado(T: float, interv: list, lamdas: list, lamda_t):
    j, nt, eventos = 0, 0, []
    t = -math.log(1 - random.random()) / lamdas[j]
    while t <= T:
        if t <= interv[j]:
            v = random.random()
            if v < lamda_t(t) / lamdas[j]:
                nt += 1
                eventos.append(t)
            t += -math.log(1 - random.random()) / lamdas[j]
        else:
            t = interv[j] + (t - interv[j]) * lamdas[j] / lamdas[j + 1]
            j += 1
    return nt, eventos


def lamda_t(t: int):
    if 0 <= t and t < 3:
        return 5 + 5*t
    elif 3 <= t and t <= 5:
        return 20
    elif 5 < t or t <= 9:
        return 30 - 2*t

def hot_dog(T):
    eventos = []
    r = Possion_adelgazamiento_mejorado(
        T=T,
        interv=[1, 2, 6, 8, 9],
        lamdas=[10,15,20,18,14],
        lamda_t=lamda_t
    )
    eventos.append(r[1])
    return eventos

def estimacion_numero_arrivos():
    sum = 0
    for _ in range(10_000):
        sum += len(hot_dog(T=9))
    print(f'El numero esperado de arribos {sum / 10_000}')

estimacion_numero_arrivos()