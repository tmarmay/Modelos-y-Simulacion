import random 
import numpy as np 

def g(x: float) -> float:
    return 1 / ( np.exp(x) - np.log(x))
    
def monte_carlo(nsim: int):
    sum = 0 
    for _ in range(nsim):
        u = random.random()
        sum += g(1/u) / (u ** 2)
    return sum / nsim

print(f'El valor exacto de la integral es {0.3944}')
ns = [1000, 10_000, 100_000]
for n in ns:
    print(f'El valor aprox de la integral es {monte_carlo(nsim=n)} en {n} sim')