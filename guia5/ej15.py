import random
import math


def Possion_no_homogeneo_adelgazamiento(T: float, lamda: float, lamda_t):
    nt, eventos = 0, []
    u = 1 - random.random()
    t = -math.log(u) / lamda
    while t <= T:
        v = random.random()
        if v < lamda_t(t) / lamda:
            nt += 1
            eventos.append(t)
        t += -math.log(1 - random.random()) / lamda
    return nt, eventos


def Possion_adelgazamiento_mejorado(T: float, interv: list, lamdas: list, lamda_t):
    j, nt, eventos = 0, 0, []
    t = -math.log(1 - random.random()) / lamdas[j]
    while t <= T:
        if t <= interv[j]:
            v = random.random()
            if v < lamda_t(t) / lamdas[j]:
                nt += 1
                eventos.append(t)
            t += -math.log(1 - random.random()) / lamdas[j]
        else:
            t = interv[j] + (t - interv[j]) * lamdas[j] / lamdas[j + 1]
            j += 1
    return nt, eventos


lamda_t = lambda x: 3 + 4 / (x + 1)
# print(Possion_no_homogeneo_adelgazamiento(T=3, lamda=7, lamda_t=lamda_t))
print(
    Possion_adelgazamiento_mejorado(
        T=1, interv=[1, 2, 3], lamdas=[7, 5, 13 / 3], lamda_t=lamda_t
    )
)
