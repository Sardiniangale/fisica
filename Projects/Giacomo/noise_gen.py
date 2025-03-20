import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import time

#parameters
RESOLUTION = 9000  #use with caution
NUM_TERMS = 100     
RANDOM_SEED = 42

#random seed
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

def generate_complex_function(x, y):
    """
    Generates a complex mathematical function using random combinations
    of various operations and coefficients
    """
    z = np.zeros_like(x)
    
    for _ in range(NUM_TERMS):
        coeff = random.uniform(-2, 2)
        freq = random.uniform(0.5, 10)
        phase = random.uniform(-np.pi, np.pi)
        scale = random.uniform(0.1, 5)
        power = random.randint(1, 5)
        
        # Randomly select operation type
        operation = random.choice([
            'trig_sin', 'trig_cos', 'exponential', 
            'polynomial', 'hyperbolic', 'gaussian',
            'product', 'modulus', 'radial'
        ])
        
        # Generate random arguments
        arg1 = random.choice([x, y, x+y, x-y, x*y])
        arg2 = random.choice([x, y, x+y, x*y, np.abs(x), np.abs(y)])
        
        # Apply selected operation
        if operation == 'trig_sin':
            term = coeff * np.sin(freq*arg1 + phase)
        elif operation == 'trig_cos':
            term = coeff * np.cos(freq*arg1 + phase)
        elif operation == 'exponential':
            term = coeff * np.exp(-scale*(arg1**2 + arg2**2))
        elif operation == 'polynomial':
            term = coeff * (arg1**power + arg2**(power//2 + 1))
        elif operation == 'hyperbolic':
            term = coeff * np.tanh(scale*arg1 + phase)
        elif operation == 'gaussian':
            term = coeff * np.exp(-((x - phase)**2 + (y - phase)**2)/(2*scale**2))
        elif operation == 'product':
            term = coeff * np.sin(freq*arg1) * np.cos(freq*arg2)
        elif operation == 'modulus':
            term = coeff * np.sqrt(x**2 + y**2 + scale)
        elif operation == 'radial':
            r = np.sqrt(x**2 + y**2)
            term = coeff * np.sin(freq*r + phase) * np.exp(-scale*r)
            
        z += term
        
    return z

# Generate grid
print("Generated grid")
x = np.linspace(-5, 5, RESOLUTION)
y = np.linspace(-5, 5, RESOLUTION)
X, Y = np.meshgrid(x, y)
print("Processing and computing function values")
start_time = time.time()
Z = generate_complex_function(X, Y)
computation_time = time.time() - start_time
print(f"Computation completed, {computation_time:.2f} seconds")

#plot
print("Plotting.")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Use surface plot for maximum computational intensity
surf = ax.plot_surface(X, Y, Z, cmap='viridis', rstride=10, cstride=10)
fig.colorbar(surf)

ax.set_title(f"STRESS TEST\n({NUM_TERMS} terms, {RESOLUTION}x{RESOLUTION} points)")
plt.show()
