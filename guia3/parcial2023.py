from monte_carlo import MonteCarlo
import math 
import random

#ejercicio2 
def juego(nsim):
    ganaA, ganaB = 0, 0    
    for _ in range(nsim):
        while True:
            u = random.random()
            v = random.random()

            if u > 1/2 and v < 1/2:
                ganaA += 1
                break
            elif u < 1/2 and v > 1/2:
                ganaB += 1
                break
    #print(f"A gano {ganaA} {ganaA/nsim}")
    #print(f"B gano {ganaB} {ganaB/nsim}")
    return ganaA, ganaB

def gana2tiradas(nsim):
    ganaA = 0
    for i in range(nsim):
        a, b = juego(2)
        if a != 2 and b != 2: # ni que gane las dos, ni que peirda las dos, que gane una
            ganaA += 1
    print(f"A gano en la primera o en la segunda {ganaA} de {nsim} veces {ganaA/nsim}")

gana2tiradas(10_000_000)

#ejercicio 4
def a(x: int):
    numerador = 6*x - 3
    denominador = numerador - (math.e ** numerador)
    return numerador / denominador


def II(y: int):
    x = (1/y -1) **3
    return x * (math.e ** -x) * (1/(y**2))

def I(x: int):
    x = (x-1) ** 3
    return x * (math.e ** -x)

def b(x: int):
    return I(x) + II(x) 

def pprint():
    puntos = [1000, 10000, 100000, 1000000]
    for i in puntos:
        #print(f'num sim {i}, {6*MonteCarlo(a,i)}') #a
        print(f'num sim {i}, {MonteCarlo(b,i)}') #b

#pprint()    