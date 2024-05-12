import random
import numpy as np
import time 

def SumaUniformes() -> float:
    x1 = random.random()
    x2 = random.random()
    return x1 + x2

def TI() -> float:
    u = 2*random.random()
    if u < 1:
        return np.sqrt(2*u)
    else:
        return 2 - np.sqrt(2 - 2*u)

def AyR() -> float:
    u = random.random() * 2
    return u

def test(*, k: int):
    su, ti, ayr = 0, 0, 0
    for _ in range(k):
        su += SumaUniformes()
        ti += TI()
        ayr += AyR()
    print(f"La esperanza teorica es {1}")
    print(f"La esperanza con {k} iteraciones es para suma de unifromes: {su/k}")
    print(f"La esperanza con {k} iteraciones es para trasnformada inversa: {ti/k}")
    print(f"La esperanza con {k} iteraciones es para rechazo: {ayr/k}")

def test2(*, k: int):
    su, ti, ayr = 0, 0, 0
    for _ in range(k):
        if SumaUniformes() > 1.5:
            su += 1
        if TI() > 1.5:
            ti += 1
        if AyR() > 1.5:
            ayr += 1
    print(f"P(X > 1.5) teorica es {0.125}")
    print(f"P(X > 1.5) con {k} iteraciones para suma de uniformes: {su/k}")
    print(f"P(X > 1.5) con {k} iteraciones para trasnformada inversa: {ti/k}")
    print(f"P(X > 1.5) con {k} iteraciones para rechazo: {ayr/k}")

test2(k=10_000)
