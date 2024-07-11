import math 
import random
import numpy as np 

#EJERCICIO 2
def poss2(x: float, m: float) -> float:
    t1 = np.exp(-m)
    t2 = (m) ** x
    t3 = math.factorial(x)
    return t1 * (t2 / t3)

#print(poss2(4, 31/8))

#EJERCICIO 3

def g(x: float) -> float:
    return 1 / ((x ** 2) * np.log(x+1))

def monte_carlo(g, nsim: int):
    integral = 0
    for _ in range(nsim):
        u = random.random()
        integral += g(1/u) / (u ** 2)

    return integral / nsim

puntos = [1000, 10000, 100000]
print(f'El valor de la integral es {0.8918}')
for i in puntos:
    resultado = monte_carlo(g, i)
    print(f'n = {i} rta = {resultado}')