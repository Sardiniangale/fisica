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
    final_x, final_y = points[-1]
    distance = np.sqrt(final_x**2 + final_y**2)
    return points, distance

# Run the initial simulation and plot
points, dist = simulate_walk(verbose=True)

x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'bo-', markersize=8, label='Path')
plt.plot(x_coords[0], y_coords[0], 'go', markersize=8, label='Origin')

# Annotate each step
for i, (x, y) in enumerate(points):
    plt.text(x, y, f' {i}', fontsize=12, ha='left', va='bottom')

plt.title('Random Walk')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# Run 1000 simulations and collect distances
distances = []
for _ in range(1000):
    _, distance = simulate_walk(verbose=False)
    distances.append(distance)

# Plot histogram with Gaussian fit
plt.figure(figsize=(8, 6))
mu = np.mean(distances)
sigma = np.std(distances)

count, bins, _ = plt.hist(distances, bins=30, density=True, alpha=0.6, color='g', label='Distance Distribution')

# Gaussian fit
x = np.linspace(min(distances), max(distances), 100)
gaussian = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))
plt.plot(x, gaussian, 'r-', linewidth=2, label='Gaussian Fit')

plt.title('Distribution of Distances from Origin after 100 Steps')
plt.xlabel('Distance')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
