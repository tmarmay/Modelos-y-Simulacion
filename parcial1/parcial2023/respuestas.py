import random 
import numpy as np 
import math 

#EJERCICIO 2
def ej2(nsim: int):
    sum = 0
    for _ in range(nsim):
        while True:
            u1, v1 = random.random(), random.random()
            u2, v2 = random.random(), random.random()
            if u1 > 0.5 and v1 < 0.5: #gana A primera y no segunda
                if u2 < 0.5 and v2 > 0.5: 
                    sum += 1
                    break
                else:
                    break
            elif u1 < 0.5 and v1 > 0.5: #gana B primera y no segunda
                if u2 > 0.5 and v2 < 0.5:
                    sum += 1
                    break
                else:
                    break
    return sum / nsim

#print(ej2(nsim=1000))

#EJERCICIO 3
def poss(x: float, lamda: float, t: float) -> float:
    t1 = np.exp(-lamda * t)
    t2 = (lamda * t ) ** x
    t3= math.factorial(x)
    return t1 * (t2 / t3)

#EJERCICIO 4
def g(x: float) -> float:
    return x / (x - np.exp(x))

def ej4a(nsim: int, g):
    sum = 0 
    for _ in range(nsim):
        u = -3 + 6 * random.random()
        sum += g(u)
    print(f'El valor exacto de la integral es {1.103}')
    print(f'El valor aprox de la integral es {(6/nsim) * sum }')

ej4a(10_0000, g)

def ej4b(nsim: int, g1, g2):
    sum1 = 0 
    sum2 = 0
    for _ in range(nsim):
        u = random.random()
        sum1 += g1(u)
        sum2 += g2(u)

    print(f'El valor exacto de la integral es {-0.16}')
    print(f'El valor aprox es {(sum1 / nsim) + (sum2 / nsim)}')

def g1(u):
    u = u -1
    return (u ** 3) * np.exp(-(u ** 3))

def g2(u):
    y = (1/u) - 1
    return  ((y ** 3) * np.exp(- (y ** 3)) ) / (u ** 2)

#ej4b(10_000, g1,g2)