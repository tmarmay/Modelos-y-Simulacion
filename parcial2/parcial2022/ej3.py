import random


def AyR():
    while True:
        y = 2 * random.random() - 1
        u = random.random()
        if u < 1 - y**2:
            return y


def test_esperanza():
    sum = 0
    for _ in range(1000):
        sum += AyR()
    print(f"El valor esperado teorico es 0")
    print(f"El valor esperado simulado es {sum/1000}")


def prob():
    sum = 0
    for _ in range(10_000):
        if AyR() > 0:
            sum += 1
    print("Teoricamente P(X > 0) = 0.5")
    print(f"Por simulacion P(X > 0) = {sum/10_000}")


prob()
