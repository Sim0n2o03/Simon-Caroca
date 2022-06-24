from operator import le
import numpy as np
from numpy import random

impares= 0
total=0
mA=random.randint(0,301,(10))
mB=random.randint(0,301,(10))

print(f"La suma de los elementos del primer arreglo es {mA.sum()}")
print(f"La suma del arreglo B es {mB.sum()}")



print(f"El total de la suma de ambos elementos es {mA.sum() + mB.sum()}")

for i in range(10):
    if mB[i]%2 !=0:
        print(f"Elementos impares {mB[i]}")

for x in range(10):
    if mB[x]%2 !=0:
        print(f"Elementos impares multiplicados *3: {mB[x]*3}")