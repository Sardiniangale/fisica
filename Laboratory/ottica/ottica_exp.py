import numpy as np
import matplotlib.pyplot as plt


sinai=[2, 5, 6, 8, 10, 12, 14, 16, 18, 26]
unceirtanty=(1)
sinar=[0.5, 3.4, 4, 5.4, 7, 8, 10, 12, 12.2, 18]



x = sinar
y = sinai
yerr = unceirtanty 
xerr = unceirtanty


fig, ax = plt.subplots()
ax.errorbar(x, y, yerr, xerr, fmt='o', linewidth=1, capsize=2)





coefficients = np.polyfit(x, y, 1)
fit_line = np.poly1d(coefficients)

x_fit = np.linspace(min(x), max(x), 100)


ax.plot(x_fit, fit_line(x_fit), 'r--', label=f'y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}')



ax.set(xlim=(0, 20), ylim=(0, 30))
ax.legend(loc='lower right')

plt.show()
