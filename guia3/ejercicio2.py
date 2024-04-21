import random

def simulacion():
    U = random.random()
    w1_2 = random.random() + random.random()

    if U < 0.5:
        return w1_2
    else:
        w3 = random.random()
        return w1_2 + w3

def experimento():
    experimentos = 1_000_000
    victoria = 0
    puntos = [100, 1000, 10000, 100000, 1000000]
    for i in range(experimentos):
        X = simulacion()
        if X >= 1:
            victoria += 1
        
        if i in puntos:
            print(f"n = {i} prob = {victoria/i}")

experimento()