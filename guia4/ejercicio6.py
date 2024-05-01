from ejercicio5 import BinomialTI
import random
import time


def GeneraXTI() -> int:
    U = random.random()
    if 0.45 <= U < 0.8:
        return 3
    elif 0.8 <= U:
        return 4
    elif 0.1 <= U < 0.35:
        return 1
    elif 0 <= U < 0.15:
        return 0
    else:
        return 2


def GeneraXAyR(c: float, n: int, p: float, vprob: list) -> int:
    while True:
        y = BinomialTI(n, p)
        if random.random() < vprob[y] / c:
            return y


"""
Como llamarlas
GeneraXAyR(c=0.84, n=4, p=0.45, vprob=vprob)
GeneraXTI()
"""
vprob = [0.15, 0.2, 0.1, 0.35, 0.2]


def ComparaSimulaciones(n: int):
    comienzo = time.time()
    for _ in range(n):
        GeneraXTI()
    final = time.time()
    print(
        f"Tiempo de ejecucion para n = {n} con metodo de transformada a la inversa: {final-comienzo}"
    )

    comienzo = time.time()
    for _ in range(n):
        GeneraXAyR(c=0.84, n=4, p=0.45, vprob=vprob)
    final = time.time()
    print(
        f"Tiempo de ejecucion para n = {n} con metodo de aceptacion y rechazo: {final-comienzo}"
    )


ComparaSimulaciones(10000)
