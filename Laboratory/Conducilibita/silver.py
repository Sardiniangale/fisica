import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_model(x, m, q):
    return m * x + q

# Insert data here
x_silver = np.array([7.0, 14.5, 22.0, 29.5, 37.0])
sigma_x_silver = np.full_like(x_silver, 0.05)
T_silver = np.array([43.41, 39.31, 34.31, 30.11, 25.65])
sigma_T_silver = np.full_like(T_silver, 0.006)

# Processing silver 
popt_silver, pcov_silver = curve_fit(linear_model, x_silver, T_silver, sigma=sigma_T_silver)
m_silver, q_silver = popt_silver
x_fit_silver = np.linspace(0, 40, 100)
plt.figure('Silver | Temperature vs Position')
plt.errorbar(x_silver, T_silver, xerr=sigma_x_silver, yerr=sigma_T_silver, fmt='o', color='orange', label='ODS Retrived Data')
plt.plot(x_fit_silver, linear_model(x_fit_silver, m_silver, q_silver), 'b-', label=f'Fit: $T = {m_silver:.3f}x + {q_silver:.3f}$')
plt.xlabel('Distance cm')
plt.ylabel('Temperature C')
plt.title('Silver |  Temperature vs Position')
plt.grid(ls='dashed', color='gray')
plt.legend()
plt.savefig('silver_temperature_position.pdf')
plt.show()
