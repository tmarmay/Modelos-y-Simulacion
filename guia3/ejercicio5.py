import math
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from monte_carlo import MonteCarlo2Dim, MonteCarlo


# b)
def b(x: int) -> int:
    return (x + 2) / (((x + 2) ** 2) - 1)


# print(MonteCarlo(b, 10000))


# c)
def c(x: int) -> int:
    t1 = 1 / x - 1
    t2 = (1 + t1**2) ** -2
    t3 = (t1 * t2) / (x**2)
    return t3


# print(MonteCarlo(c, 10000))


# d) mal
def d(x: int) -> int:
    t1 = -(1 / x) + 1
    t1 = math.e ** -(t1**2)
    t1 = t1 * ((-x + 1) ** 2)

    t2 = (1 / x) - 1
    t2 = math.e ** -(t2**2)
    t2 = t2 * ((x + 1) ** 2)

    return t1 + t2


# print(MonteCarlo(d, 100000))


# e)
def e(x: int, y: int) -> int:
    z = (x + y) ** 2
    return math.e**z


# print(MonteCarlo2Dim(e, 1000))


# f)
def f(x: int, y: int) -> int:
    t1 = (-2 / x) + 2
    t2 = (-1 / x) + 1
    t3 = 1 / (x + 1)
    return ((math.e**t1) - (math.e**t2)) / (t3**2)


print(-MonteCarlo2Dim(f, 10000))
