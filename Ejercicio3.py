from array import array
import numpy as np 
from numpy import random

V=0
C=0

Arreglo=np.array([["t","m","i","o"],["p","r","f","e"],["k","a","i","x"],["s","j","o","n"]])

print(Arreglo)
for x in range(4):
    for y in range(4):
        if(Arreglo[x][y]=="a" or  Arreglo[x][y]=="e" or Arreglo[x][y]=="i" or Arreglo[x][y]=="o" or  Arreglo[x][y]=="u"):
                V=V+1

print(f"El total de vocales es {V}")

