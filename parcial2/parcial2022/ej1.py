import random


def urna():
    # p, k = [0.32, 0.32, 0.33, 0.14], 100
    p_k = [32, 21, 33, 14]
    urna = []
    for i in range(len(p_k)):
        for _ in range(p_k[i]):
            urna.append(i)

    u = int(100 * random.random())
    return urna[u]
