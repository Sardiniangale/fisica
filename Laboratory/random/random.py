import numpy as np
import matplotlib.pyplot as plt


phi = np.random.uniform(0, np.pi/2)

#to cartesian
x = np.cos(phi)
y = np.sin(phi)

print(f"Random angle: {np.degrees(theta):.2f}°")
print(f"Coordinates: ({x:.4f}, {y:.4f})")

# Plot the point
plt.figure(figsize=(5, 5))
plt.scatter(x, y, color='red', label=f'Angle: {np.degrees(theta):.2f}°')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.legend()
plt.title('Random Direction in First Quadrant (0°-90°)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
