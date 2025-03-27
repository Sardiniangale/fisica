import numpy as np
import matplotlib.pyplot as plt

Tempo = [778, 736, 694, 661, 646]
au = [0.02, 1.49, 2.91, 4.334, 5.753]

y = Tempo
x = au
yerr = 5  
xerr =  0.05

fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=yerr, xerr=xerr, fmt='o', linewidth=1, capsize=2)

# Linear fit
coefficients = np.polyfit(x, y, 1)
fit_line = np.poly1d(coefficients)
x_fit = np.linspace(min(x), max(x), 100)
ax.plot(x_fit, fit_line(x_fit), 'r--', label=f'y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}')

# Corrected axis limits
ax.set(ylim=(600, 800), xlim=(0, 6))  # Swapped limits to match x and y data
ax.legend(loc='upper right')

plt.show()
