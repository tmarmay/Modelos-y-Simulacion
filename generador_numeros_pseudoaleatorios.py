def vonNeumann(u: int) -> int:
    """
    Funcion que implementa el metodo de Von Neumann para generar numeros aleatorios.

    Parametros:
        u (int): Semilla inicial para la generacion de numeros aleatorios.

    Retorna:
        int: Numero aleatorio generado.
    """
    u = (u**2 // 100) % 1000
    return u


def randMixto(a: int, c: int, M: int, u: int) -> int:
    """
    Funcion que implementa el generador de numeros pseudoaleatorios congruencial mixto.

    Parametros:
        a (int): Multiplicador.
        c (int): Constante aditiva.
        M (int): Modulo.
        u (int): Semilla inicial.

    Retorna:
        int: Numero pseudoaleatorio generado.
    """
    return (a * u + c) % M


def randMulti(a: int, M: int, u: int) -> int:
    """
    Funcion que implementa el generador de numeros pseudoaleatorios multiplicativo.

    Parametros:
        a (int): Multiplicador.
        M (int): Modulo.
        u (int): Semilla inicial.

    Retorna:
        int: Numero pseudoaleatorio generado.
    """
    return (a * u) % M


def obtenerPeriodo(a: int, c: int, M: int, u: int, type: str) -> int:
    """
    Funcion que obtiene el periodo de un generador pseudoaleatorio congruencial mixto o multiplicativo.

    Parametros:
        gen (function): Funcion generadora de numeros pseudoaleatorios.
        a (int): Multiplicador.
        c (int): Constante aditiva.
        M (int): Modulo.
        u (int): Semilla inicial.
        type (str): Tipo de generador (mixto o multiplicativo).

    Retorna:
        int: Periodo del generador pseudoaleatorio.
    """
    if type not in ["mixto", "multiplicativo"]:
        raise ValueError("El tipo debe ser 'mixto' o 'multiplicativo'.")

    K = 0
    y_1 = randMixto(a, c, M, u) if type == "mixto" else randMulti(a, M, u)
    y_i = y_1
    while y_1 != y_i or K == 0:
        K += 1
        y_i = randMixto(a, c, M, y_i) if type == "mixto" else randMulti(a, M, y_i)
    return K


def verificaKmaximo(a: int, c: int, M: int, u: int, type: str) -> bool:
    """
    Funcion que verifica si el periodo alcanzado por un generador pseudoaleatorio
    congruencial es el maximo posible para el tipo de generador especificado.

    Parametros:
        a (int): Multiplicador.
        c (int): Constante aditiva.
        M (int): Modulo.
        u (int): Semilla inicial.
        tipo (str): Tipo de generador ('mixto' o 'multiplicativo').

    Retorna:
        bool: True si el periodo alcanzado es el maximo posible, False en caso contrario.
    """
    if type not in ["mixto", "multiplicativo"]:
        raise ValueError("El tipo debe ser 'mixto' o 'multiplicativo'.")

    K = obtenerPeriodo(a, c, M, u, type)
    resp = (K == M) if type == "mixto" else (K == M - 1)
    return resp
