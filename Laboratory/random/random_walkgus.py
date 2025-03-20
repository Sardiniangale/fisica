import numpy as np
import matplotlib.pyplot as plt

def random_journey(steps=100):
    """dxd"""
    x, y = 0.0, 0.0
    #step math
    for step in range(steps):
        angle = np.random.uniform(0, 2 * np.pi)
        dx = np.cos(angle)
        dy = np.sin(angle)
        x += dx
        y += dy
        # (Kept the original math, just removed printing/plotting)
    return np.sqrt(x**2 + y**2)  #fin distance

# 200 cigarets 
distances = [random_journey(100) for _ in range(100000)]

plt.figure(figsize=(10, 6))

#plot histogram
plt.hist(distances, bins=100, density=True, 
        alpha=0.6, color='blue', edgecolor='black', 
        label='Walk Results')

#add a optional curve
avg_dist = np.mean(distances)
spread = np.std(distances)
x_vals = np.linspace(min(distances), max(distances), 200)
gauss_curve = (1/(spread * np.sqrt(2*np.pi))) * np.exp(-0.5*((x_vals-avg_dist)/spread)**2)

plt.plot(x_vals, gauss_curve, 'red', linewidth=2, 
        label=f'Fit: Avg = {avg_dist:.1f}\nSpread = {spread:.1f}')

#
plt.title('Random walk', pad=15, size=14)
plt.xlabel('Distance from Start', labelpad=10)
plt.ylabel('Frequency', labelpad=10)
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()
