import numpy as np
import matplotlib.pyplot as plt


phi = np.random.uniform(0, np.2*pi)
dist = 1
originx = 0
originy = 0

#to cartesian
x = np.cos(phi)
y = np.sin(phi)

print(f"Random angle: {np.degrees(phi):.2f}°")
print(f"Coordinates: ({x:.4f}, {y:.4f})")

# Plot the point
plt.figure(figsize=(-5, 5))
plt.scatter(x, y, color='red', label=f'Angle: {np.degrees(phi):.2f}°')



plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.grid(True)
plt.legend()
plt.title('bob')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
