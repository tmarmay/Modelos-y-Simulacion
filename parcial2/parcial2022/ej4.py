import random
import math


def px(n: int):
    t = 2 ** (n - 1) + 2
    return t / (3**n)


def a():
    print(f"P(X = 4) = {px(4)}")


def GeneraGeo():
    U = random.random()
    return int(math.log(1 - U) / math.log(2 / 3)) + 1


def pGeo(x: int):
    return (1 / 3) * ((2 / 3) ** (x - 1))


def AyR():
    while True:
        y = GeneraGeo()
        while y < 2:
            y = GeneraGeo()
        u = random.random()
        if u < px(y) / (2 * pGeo(y)):
            return y


def prob():
    sum = 0
    for _ in range(10_000):
        if AyR() == 4:
            sum += 1
    print(f"Teoricamente P(X == 4) = {px(4)}")
    print(f"Por simulacion P(X == 0) = {sum/10_000}")


prob()
    