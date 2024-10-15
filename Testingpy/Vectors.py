import numpy as np


def vector_addition_r3():

    print("Cosa sono le coordinate del 1st vettore (x, y, z):")
    x1 = float(input("x: "))
    y1 = float(input("y: "))
    z1 = float(input("z: "))


    print("Cosa sono le coordinate del 2nd vettore (x, y, z):")
    x2 = float(input("x: "))
    y2 = float(input("y: "))
    z2 = float(input("z: "))

    
    v1 = np.array([x1, y1, z1])
    v2 = np.array([x2, y2, z2])

   
    x = v1 + v2

    print("La somma dei due vettori e:", x)



#I stole this, no idea why its needed
if __name__ == "__main__":
    vector_addition_r3()