import random

def trasnf_inv():
    u = random.random()
    if u < 0.5:
        return 4*u
    else:
        return - 1 / (u-1)

def prob(n: int):
    sum = 0
    for _ in range(n):
        if trasnf_inv() <= 3:
            sum += 1
    print(f'La probabilidad teorica de P(X <= 3) es {2/3}')
    print(f'La probabilidad usando trasformada inversa de P(X <= 3) es {sum / n}')

prob(n=10_000)