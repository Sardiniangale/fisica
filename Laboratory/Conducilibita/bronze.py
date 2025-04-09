import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_model(x, m, q):
    return m * x + q

# ARRRAY FOR BRONZE DATA
x_bronze = np.array([6.5, 12.9, 19.4, 25.8, 32.3, 38.75, 45.2])
sigma_x_bronze = np.full_like(x_bronze, 0.05)
T_bronze = np.array([38.47, 37.18, 34.31, 32.08, 29.79, 27.65, 25.44])
sigma_T_bronze = np.full_like(T_bronze, 0.006)

# Bronze DATA PROCCESSING
popt_bronze, pcov_bronze = curve_fit(linear_model, x_bronze, T_bronze, sigma=sigma_T_bronze)
m_bronze, q_bronze = popt_bronze
x_fit_bronze = np.linspace(0, 50, 100)
plt.figure('Bronze | Temperature vs Distance')
plt.errorbar(x_bronze, T_bronze, xerr=sigma_x_bronze, yerr=sigma_T_bronze, fmt='o', label='ODS Retrived Data')
plt.plot(x_fit_bronze, linear_model(x_fit_bronze, m_bronze, q_bronze), 'r-', label=f'Fit: $T = {m_bronze:.3f}x + {q_bronze:.3f}$')
plt.xlabel('Distance cm')
plt.ylabel('Temperature C')
plt.title('Bronze | Temperature vs Position')
plt.grid(ls='dashed', color='gray')
plt.legend()
plt.savefig('bronze_temperature_position.pdf')
plt.show()
