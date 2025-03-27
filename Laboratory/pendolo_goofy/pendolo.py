import numpy as np
import matplotlib.pyplot as plt

Tempo = [0.02, 1.5, 2.91, 4.33, 5.75]
au = [778, 736, 694, 661, 646]

x = Tempo
y = au
yerr = 5  
xerr =  0.05



fig, ax = plt.subplots()
ax.errorbar(x, y, yerr, xerr, fmt='o', linewidth=1, capsize=2)




coefficients = np.polyfit(x, y, 1)
fit_line = np.poly1d(coefficients)

x_fit = np.linspace(min(x), max(x), 100)
ax.plot(x_fit, fit_line(x_fit), 'r--', label=f'y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}')


ax.set(xlim=(0, 6), ylim=(600, 800))
ax.legend(loc='upper right')  

plt.show()
