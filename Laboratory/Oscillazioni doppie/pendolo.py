import numpy as np
import matplotlib.pyplot as plt

Tempo = [0.03, 1.7, 3.12, 4.54, 5.96]
au = [819, 814, 810, 804, 800]

Tempo2 = [0.02, 1.49, 2.91, 4.334, 5.753]
au2 = [778, 736, 694, 661, 646]

yerr = 5
xerr = 0.05

fig, ax = plt.subplots()

# Plot first dataset with error bars and fit line
ax.errorbar(Tempo, au, yerr=yerr, xerr=xerr, fmt='o', color='red', label='Dataset 1', capsize=4)
coeff1 = np.polyfit(Tempo, au, 1)
fit1 = np.poly1d(coeff1)
x_fit1 = np.linspace(min(Tempo), max(Tempo), 100)
ax.plot(x_fit1, fit1(x_fit1), 'r--', label=f'Fit 1: {coeff1[0]:.1f}x + {coeff1[1]:.1f}')

# Plot second dataset with error bars and fit line
ax.errorbar(Tempo2, au2, yerr=yerr, xerr=xerr, fmt='s', color='blue', label='Dataset 2', capsize=4)
coeff2 = np.polyfit(Tempo2, au2, 1)
fit2 = np.poly1d(coeff2)
x_fit2 = np.linspace(min(Tempo2), max(Tempo2), 100)
ax.plot(x_fit2, fit2(x_fit2), 'b--', label=f'Fit 2: {coeff2[0]:.1f}x + {coeff2[1]:.1f}')

ax.set(xlim=(0, 6), ylim=(600, 1000),
       xlabel='Time (units)', ylabel='AU',
       title='Comparison of Two Datasets')
ax.legend(loc='upper right', frameon=True)
ax.grid(True, linestyle='--', alpha=0.7)

plt.show()
