import numpy as np
import matplotlib.pyplot as plt

def random_step(origin=(0, 0)):
    """Generate a new point 1 unit away from origin in random direction"""
    theta = np.random.uniform(0, 2*np.pi)  # Full circle angle
    dx, dy = np.cos(theta), np.sin(theta)
    return (origin[0] + dx, origin[1] + dy)

def plot_recursive_walk(num_steps=5):
    """Plot recursive random walk with specified number of steps"""
    plt.figure(figsize=(8, 8))
    current_pos = (0, 0)
    
    # Plot origin
    plt.scatter(*current_pos, color='black', s=100, label='Origin (0,0)')
    
    # Create colormap for progression
    colors = plt.cm.viridis(np.linspace(0, 1, num_steps))
    
    for i in range(num_steps):
        new_pos = random_step(current_pos)
        
        # Plot the step
        plt.plot([current_pos[0], new_pos[0]], 
                 [current_pos[1], new_pos[1]], 
                 color=colors[i], 
                 marker='o',
                 label=f'Step {i+1}')
        
        # Update origin for next step
        current_pos = new_pos
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Recursive Random Walk ({num_steps} Steps)')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# Generate and plot a 5-step recursive walk
plot_recursive_walk(5)
