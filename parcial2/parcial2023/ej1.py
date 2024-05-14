import random

def trasnf_inv():
    p = [0.24, 0.09, 0.31, 0.36]
    i, F, u = 0, p[0], random.random()

    while u >= F:
        i += 1
        F += p[i]
    return i

def variableX():
    u = random.random()
    v = random.random()

    if u < 0.3:
        if v < 0.8: return 0
        else: return 2
    elif u < 0.75:
        if v < 0.2: return 1
        else: return 3
    else: return 2

def test(n: int):
    sum1, sum2 = 0, 0
    for _ in range(n):
        sum1 += trasnf_inv()
        sum2 += variableX()
    print(f"Promedio variableX = {sum2/n}")
    print(f"Promedio transf_inv = {sum1/n}")

test(10_000)