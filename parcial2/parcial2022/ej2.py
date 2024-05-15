import math
import random
import numpy as np


def ti():
    u = random.random()
    if u < 1 / 3:
        return math.log(3 * u)
    else:
        t = 1.5 * (1 - u)
        return -math.log(t) / 2


def test_esperanza():
    sum = 0
    for _ in range(1000):
        sum += ti()
    print(f"El valor esperado teorico es 0")
    print(f"El valor esperado simulado es {sum/1000}")


def prob():
    sum = 0
    for _ in range(10_000):
        if ti() <= 1:
            sum += 1
    print(f"Teoricamente P(X <= 1) = {1 - (2/3) * np.exp(-2)}")
    print(f"Por simulacion P(X <= 1) = {sum/10_000}")


prob()
