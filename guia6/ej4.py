import random

#INCOMPLETO
def N():
    n, sum = 0, 0
    while sum <= 1:
        sum += random.random()
        n += 1
    return n

def Media_Muestral_X(g, Nsim: int) -> float:
    media, scuad, n = 0, 0, 0
    for n in range(2, Nsim):
        n += 1
        x = g()
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return n, media, scuad

def test(Nsim: int):
    n, media, scuad = Media_Muestral_X(N, Nsim)
    print(f'Estimacion de N con {Nsim} simulaciones: {media}')

test(1000)