'''
Created on 16 Oct 2024

@author: Giacomo
'''
import numpy as np


loops = int(input("Amount of vectors needed?: "))

def vector_addition_r3():



lis = []

for x in range(loops):
    
    x1 = float(input("x: "))
    y1 = float(input("y: "))
    z1 = float(input("z: "))
    
    x2 = float(input("x: "))
    y2 = float(input("y: "))
    z2 = float(input("z: "))
    
    v1 = np.array([x1, y1, z1])
    v2 = np.array([x2, y2, z2])
  
  b = v1 + v2 
  
  
  
  
print("La somma dei vettori e:", b)



#I stole this, no idea why its needed
if __name__ == "__main__":
    vector_addition_r3()