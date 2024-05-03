import random
import math 
import numpy as np 
from matplotlib import pyplot as plt

def PoissonTI(lamda: int) -> int:
    U = random.random()
    i, p = 0, (math.e ** -lamda)
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p
    return i

def PoissonTIop(lamda: int) -> int:
    p = math.e ** -lamda
    F = p
    for j in range(1, int(lamda) + 1):
        p *= lamda / j
        F += p
    U = random.random()
    if U >= F:
        j = int(lamda) + 1
        while U >= F:
            p *= lamda / j 
            F += p
            j += 1
        return j-1
    else:
        j = int(lamda)
        while U < F:
            F -= p
            p *= j / lamda
            j -= 1
        return j + 1

def Comparacion():
    valoresTi = np.zeros(30)
    valoresTiop = np.zeros(30)

    for _ in range(1000):
        xti = PoissonTI(lamda=10)
        valoresTi[xti] += 1

        xtiop = PoissonTIop(lamda=10)
        valoresTiop[xtiop] += 1

    xs = [x for x in range(30)]

    plt.bar(xs, valoresTi, label='Metodo Poisson transformada inversa')
    plt.bar(xs, valoresTiop, label='Metodo Poisson transformada inversa optimizado')
    plt.legend()
    plt.show()

Comparacion()