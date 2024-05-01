import random

prob = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
urna = [
    11,11,11,11,11,11,11,11,11,11,
    11,14,14,14,14,14,14,14,14,14,
    14,14,14,14,14,9,9,9,9,9,9,9,
    9,9,8,8,8,8,8,8,8,8,12,12,12,
    12,12,12,12,12,12,12,12,12,10,
    10,10,10,10,10,10,10,10,10,9,9,
    9,9,9,9,9,9,9,7,7,7,7,7,7,7,11,
    11,11,11,11,11,11,11,11,11,11,9,
    9,9,9,9,9,9,9,9,
]


def AceptacionRechazo() -> int:
    """
    Implementación del método de aceptación rechazo para generar variables aleatorias.

    Returns:
        int: Variable aleatoria generada.

    Notas:
        - La función utiliza el método de aceptación rechazo para generar una variable aleatoria
          basada en una distribución de probabilidad dada.
        - La distribución de probabilidad está representada por la lista 'prob'.
        - 'c' es una constante de normalización para la distribución de probabilidad.
        - 'qj' es un valor de control para el método de aceptación rechazo.
        - La variable aleatoria generada se retorna una vez que se cumple la condición de aceptación.

    Ejemplo:
        Para generar una variable aleatoria utilizando esta función, simplemente llámala así:
        >>> variable_aleatoria = MyR()

    """
    # Y ~ U(1,10) => qj = 0.1
    # 0.14/0.1 <= c
    c, qj = 1.4, 0.1
    while True: #PREGUNTAR SI EL WHILE VA ABAJO DE ESTA LINEA O DONDE ESTA
        Y = int(random.random() * 10) + 1
        if random.random() < prob[Y - 1] / (c * qj):
            return Y


def TransformadaInversa(p: list, xs: list) -> int:
    """
    Implementación del método de la transformada inversa para generar variables aleatorias.

    Args:
        p (list): Lista de probabilidades.
        xs (list): Lista de valores correspondientes a las probabilidades acumuladas.

    Returns:
        int: Variable aleatoria generada.

    Notas:
        - Este método utiliza la transformada inversa para generar una variable aleatoria
          basada en una distribución discreta de probabilidad.
        - La lista 'p' representa las probabilidades de los valores posibles.
        - La lista 'xs' contiene los valores correspondientes a las probabilidades.
        - Se genera un número aleatorio U entre 0 y 1.
        - Se selecciona el valor correspondiente de 'xs' basado en el valor de 'p' que
          coincide con el intervalo en el que cae U.

    Ejemplo:
        Para generar una variable aleatoria utilizando esta función, simplemente llámala así:
        >>> variable_aleatoria = TransformadaInversa([0.1, 0.5, 0.3, 0.1], [1, 2, 3, 4])
    """
    U = random.random()
    i, F = 0, p[0]
    while U >= F:
        i += 1
        F += p[i]
    return xs[i]


def MetodoUrna(k) -> int:
    """
    Implementación del método de la urna para generar variables aleatorias.

    Args:
        k (int): Número de elementos en la urna.

    Returns:
        int: Variable aleatoria generada.

    Notas:
        - Este método utiliza el método de la urna para generar una variable aleatoria
          basada en una urna con 'k' elementos.
        - Se genera un número aleatorio U entre 0 y 1.
        - Se utiliza U para seleccionar un elemento de la urna.
        - El índice del elemento seleccionado se calcula multiplicando U por 'k' y
          tomando la parte entera de este resultado.

    Ejemplo:
        Para generar una variable aleatoria utilizando esta función, simplemente llámala así:
        >>> variable_aleatoria = MetodoUrna(10)
    """
    U = random.random()
    return urna[int(U) * k]
