import numpy as np
import matplotlib.pyplot as plt

def simulate_walk(verbose=False):
    points = [(0.0, 0.0)]
    for step in range(100):
        phi = np.random.uniform(0, 2 * np.pi)
        dx = np.cos(phi)
        dy = np.sin(phi)
        new_x = points[-1][0] + dx
        new_y = points[-1][1] + dy
        points.append((new_x, new_y))
        
        if verbose:
            print(f"Step {step + 1}:")
            print(f"Random angle: {np.degrees(phi):.2f}°")
            print(f"New coordinates: ({new_x:.4f}, {new_y:.4f})\n")
    
    # Calculate final distance after all steps
    final_x, final_y = points[-1]
    distance = np.sqrt(final_x**2 + final_y**2)
    return points, distance

# Initial simulation and plot
points, _ = simulate_walk(verbose=True)

# Plot setup
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'bo-', markersize=8, label='Path')
plt.plot(x_coords[0], y_coords[0], 'go', markersize=8, label='Origin')

# Annotate steps
for i, (x, y) in enumerate(points):
    plt.text(x, y, f' {i}', fontsize=12, ha='left', va='bottom')

plt.title('Random Walk Visualization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Run 1000 simulations
distances = []
for _ in range(1000):
    _, distance = simulate_walk()
    distances.append(distance)

# Statistical analysis
mu = np.mean(distances)
sigma = np.std(distances)

# Histogram plot
plt.figure(figsize=(8, 6))
count, bins, _ = plt.hist(distances, bins=30, density=True, 
                         alpha=0.6, color='teal', label='Distance Frequency')

# Gaussian curve overlay
x = np.linspace(min(distances), max(distances), 100)
gaussian = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))
plt.plot(x, gaussian, 'maroon', linewidth=2, label='Normal Distribution')

plt.title('Gaussian Distribution of Final Distances')
plt.xlabel('Distance from Origin')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
