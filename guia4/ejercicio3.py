import numpy as np
import random 


def SimulaTiradaDados():
    a = np.zeros(12)
    it = 0
    while np.sum(a) != 12:
        dado1 = random.randrange(0,7)
        dado2 = random.randrange(0,7)
        a[dado1+dado2-1] = 1
        it += 1
    return it

def DatosEspatisitcosExperimento(n):
    a = np.zeros(n)
    for i in range(n):
        a[i] = SimulaTiradaDados()
    print(f'En promedio, hizo falta tirar {np.average(a)} veces para sacar todos los numeros')
    print(f'La desviacion estandar fue de {np.std(a)}')


for i in [100, 1000, 10000]:
    print(f'Para n = {i}')
    DatosEspatisitcosExperimento(i)
    print('--- '*4)