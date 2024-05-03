import random
import math 
from functools import reduce

def Possion(lamda: float, i: int) -> float:
    return (math.e ** -lamda) * (lamda**i) * (1/math.factorial(i))

def DistribucionTI(k: int, lamda: int) -> int:
    U = random.random()
    c = reduce(lambda x,y: x + Possion(lamda, y), [x for x in range(k+1)] )
    i, p = 0, (math.e ** -lamda) / c
    F = p
    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p
    return i

print(DistribucionTI(4, 10))
