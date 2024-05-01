import math
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from monte_carlo import MonteCarlo2Dim, MonteCarlo


def a(x: int, y: int):
    return 1 - (math.e ** (-x - y))


def I(y: int):
    x = (1 / y - 1) ** 2
    return x * (math.e**-x) * (1 / (y**2))


def II(x: int):
    return (x**2) * (math.e ** (-(x**2)))


def b(x: int):
    return I(x) - II(x)


def pprint():
    puntos = [1000, 10000, 100000, 1000000]
    for i in puntos:
        # print(f'num sim {i}, {MonteCarlo2Dim(a,i)}') #a)
        # No estoy 100% seguro porque funciona de las dos formas
        print(f"num sim {i}, {MonteCarlo(I,i) - MonteCarlo(II,i)}")  # b)
        print(f"num sim {i}, {MonteCarlo(b,i)}")  # b)


pprint()
