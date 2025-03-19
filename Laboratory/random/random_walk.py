import numpy as np
import matplotlib.pyplot as plt

#start point
points = [(0.0, 0.0)]

for step in range(3):
    #random angle
    phi = np.random.uniform(0, 2 * np.pi)
    dx = np.cos(phi)
    dy = np.sin(phi)
    
    #delta origin
    new_x = points[-1][0] + dx
    new_y = points[-1][1] + dy
    points.append((new_x, new_y))
    
    #new angle
    print(f"Step {step + 1}:")
    print(f"Random angle: {np.degrees(phi):.2f}°")
    print(f"New coordinates: ({new_x:.4f}, {new_y:.4f})\n")

x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

#plot
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'bo-', markersize=8, label='path')
plt.plot(x_coords[0], y_coords[0], 'go', markersize=8, label='start')

for i, (x, y) in enumerate(points):
    plt.text(x, y, f' {i}', fontsize=12, ha='left', va='bottom')

plt.title('3-Step Random Walk with Unit Length Steps')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
