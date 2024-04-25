import math 
import random

def I(x):
    t1 = ((1/x) - 1) ** 2
    t2  =  math.log(1/x) 
    t3 = x ** 2
    return 1 / (t1 * t2 * t3)

def II(x):
    t1 = x ** 2
    t2 = math.log(x + 1)
    return 1 / (t1 * t2)

def monte_carlo(g, N):
    integral = 0
    for _ in range(N):
        integral += g(random.random())
    return integral/N

puntos = [1000, 10000, 100000]
for i in puntos:
    resultado = monte_carlo(I, i) - monte_carlo(II, i)
    print(f'n = {i} rta = {resultado}')