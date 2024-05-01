import numpy as np
import random


# b)
def SimulaTiradaDados() -> int:
    """
    Simula la tirada de dos dados hasta que se obtienen todos los números del 2 al 12 al menos una vez.

    Returns:
        int: El número de iteraciones necesarias para obtener todos los números.
    """
    a = np.zeros(12)
    it = 0
    while np.sum(a) != 12:
        dado1 = random.randrange(0, 7)
        dado2 = random.randrange(0, 7)
        a[dado1 + dado2 - 1] = 1
        it += 1
    return it


# I)
def DatosEspatisitcosExperimento(n: int):
    """
    Realiza un experimento de simulación de tiradas de dados y calcula estadísticas sobre los resultados.

    Args:
        n (int): El número de experimentos a realizar.
    """
    a = np.zeros(n)
    for i in range(n):
        a[i] = SimulaTiradaDados()
    print(
        f"En promedio, hizo falta tirar {np.average(a)} veces para sacar todos los numeros"
    )
    print(f"La desviacion estandar fue de {np.std(a)}")


# for i in [100, 1000, 10000]:
#     print(f'Para n = {i}')
#     DatosEspatisitcosExperimento(i)
#     print('--- '*4)

# II)
print("La probabilidad de que N sea por lo menos 15")
for i in [100, 1000, 10000]:
    numerador = 0
    denominador = 0
    for j in range(i):
        if SimulaTiradaDados() >= 15:
            numerador += 1
        denominador += 1
    print(f"Para n = {i}, avg = {numerador/denominador}")
    print("--- " * 4)

print("La probabilidad de que N sea a lo sumo 9")
for i in [100, 1000, 10000]:
    numerador = 0
    denominador = 0
    for j in range(i):
        if SimulaTiradaDados() <= 9:
            numerador += 1
        denominador += 1
    print(f"Para n = {i}, avg = {numerador/denominador}")
    print("--- " * 4)
