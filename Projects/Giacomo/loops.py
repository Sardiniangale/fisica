import numpy as np

def vector_addition_r3():
    while True:
        num_vectors = int(input("Quanti vettori vuoi sommare? "))





        vectors = []
        for i in range(num_vectors):
            print(f"Cosa sono le coordinate del {i+1}-esimo vettore (x, y, z):")
            x = float(input("x: "))
            y = float(input("y: "))
            z = float(input("z: "))
            vectors.append(np.array([x, y, z]))

        result = np.sum(vectors, axis=0)
        print("La somma dei vettori è:", result)


#this is actually very important

        print("\nPress 'q' to quit, or any other key to continue.")
        if input().lower() == 'q':
            break
        
        
        #closes the loop

if __name__ == "__main__":
    vector_addition_r3()