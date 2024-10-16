import numpy as np


def vector_addition_r3():

    print("Cosa sono le coordinate del primo vettore (x, y, z):")
    x1 = float(input("x: "))
    y1 = float(input("y: "))
    z1 = float(input("z: "))


    print("Cosa sono le coordinate del 2nd vettore (x, y, z):")
    x2 = float(input("x: "))
    y2 = float(input("y: "))
    z2 = float(input("z: "))

    print("Cosa sono le coordinate del 3rd vettore (x, y, z):")
    x3 = float(input("x: "))
    y3 = float(input("y: "))
    z3 = float(input("z: "))


    v1 = np.array([x1, y1, z1])
    v2 = np.array([x2, y2, z2])
    v3 = np.array([x3, y3, z3])

    b = v1 + v2 + v3

    print("La somma dei vettori e:", b)



#I stole this, no idea why its needed
if __name__ == "__main__":
    vector_addition_r3()