import numpy as np
import matplotlib.pyplot as plt

n=int(input("Enter the precision required for the graph: "))

def plot_function():
    print("Enter a mathematical function of x to plot, use regular numpy notation:")
    func_input = input("f(x) = ")

    try:
#hellaplugger
        x = np.linspace(-10, 10, n)

#Ceirtified shitter

        safe_env = {"np": np, "x": x}

#mannellas breath smells :0

        y = eval(func_input, {"__builtins__": {}}, safe_env)
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=f"f(x) = {func_input}")
        plt.title("Graph of the function")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"An error occurred, respectfully learn basic maths.")


# Call the function
plot_function()



#ceirtified shit code