import numpy as np
import matplotlib.pylab as plt

# First try making the random walk
path = [(0,0)]
for i in range(100):
    random_radian = np.random.random() * 2 * 3.1415
    x_add = np.cos(random_radian)
    y_add = np.sin(random_radian)
    
    last_x = path[-1][0]
    last_y = path[-1][1]
    new_x = last_x + x_add
    new_y = last_y + y_add
    path.append( (new_x, new_y) )
    
    print(f"Step {i+1}: Angle {np.degrees(random_radian):.1f}°")
    print(f"Moved to ({new_x:.3f}, {new_y:.3f})\n")

# Drawing part
xs = [p[0] for p in path]
ys = [p[1] for p in path]

plt.figure()
plt.plot(xs, ys, 'b-')
plt.plot(xs, ys, 'ro')
plt.title("My Walk")
plt.grid()
plt.show()

# Now do the 1000 walks part
final_distances = []

for _ in range(1000):
    temp_path = [(0,0)]
    for _ in range(100):
        rand_angle = np.random.uniform(0, 2*np.pi)
        temp_x = temp_path[-1][0] + np.cos(rand_angle)
        temp_y = temp_path[-1][1] + np.sin(rand_angle)
        temp_path.append( (temp_x, temp_y) )
    
    end_x = temp_path[-1][0]
    end_y = temp_path[-1][1]
    how_far = (end_x**2 + end_y**2)**0.5
    final_distances.append(how_far)

# Make the histogram
plt.figure()
plt.hist(final_distances, bins=25, color='orange', edgecolor='black')

avg = sum(final_distances)/len(final_distances)
std = np.std(final_distances)
x_vals = np.linspace(min(final_distances), max(final_distances), 100)
curve = np.exp(-(x_vals-avg)**2/(2*std**2)) / (std*np.sqrt(2*np.pi))  # Oops line break
plt.plot(x_vals, curve, 'r-')

plt.xlabel("How Far")
plt.ylabel("Times Happened")
plt.title("Distance Spread")
plt.show()
