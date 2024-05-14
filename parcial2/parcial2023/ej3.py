import random 
import math

k = 1 - (0.4 ** 20) # c = 1/k

def pY(i: float):
    return 0.6 * (0.4 ** (i-1))

def pX(i: float):
    if i > 20:
        return 0
    else:
        return pY(i) / k
    
def SimulaGeometrica():
    u = random.random()
    return int(math.log(1-u)/ math.log(0.4)) + 1

def esperanzaX():
    sum = 0
    for i in range(1,21):
        t1 = 0.6 * (0.4 ** (i-1))
        sum += t1/k
    return sum

def AyR(c: float, p, q, simgeo):
    while True:
        y = simgeo()
        u = random.random()
        if u < p(y) / (c * q(y)):
            return y

def test(n: int):
    sum = 0
    for _ in range(n):
        sum += AyR(1/k, pX, pY, SimulaGeometrica)
    print(f'Esperanza teorica de X {esperanzaX()}')
    print(f'Esperanza de la simulacion de X {sum/n}')

test(10_000)