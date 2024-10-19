import numpy as np

def vector_addition_r3():
    num_vectors = int(input("Quanti vettori vuoi sommare? "))

    vectors = []
    for i in range(num_vectors):
        
        #the f is used for formating, otherwise it will break. 
        
        
        print(f"Cosa sono le coordinate del {i+1}-esimo vettore (x, y, z):")
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z: "))
        vectors.append(np.array([x, y, z]))

    result = np.sum(vectors, axis=0)
    print("La somma dei vettori è:", result)



#No idea what this is needed for

if __name__ == "__main__":
    vector_addition_r3()
    
    
    #Vector calculator completed, ill compile it now
    