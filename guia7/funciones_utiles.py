import numpy as np
import math
from functools import reduce

matriz = np.array([[1 / 2, 1 / 4, 1 / 4], [1 / 3, 0, 2 / 3], [1 / 2, 1 / 2, 0]])


def elevar_n_veces_matriz(A: np.ndarray, n: int) -> np.ndarray:
    return np.linalg.matrix_power(A, n)


print(
    elevar_n_veces_matriz(
        np.array([[1/2, 1/2], [2/3, 1/3]]), 3
    )
)


def calcula_autovalores(A: np.ndarray) -> list:
    autovalores, autovectores = np.linalg.eig(A)
    return autovalores


# print(calcula_autovalores(np.array([[0, 1/2, 1/2], [1/2, 0, 1/2], [1/2, 1/2, 0]])))


def calcula_mcd(ns: list) -> int:
    mcd = reduce(math.gcd, ns)
    return mcd

#print(calcula_mcd([450,360,90]))
