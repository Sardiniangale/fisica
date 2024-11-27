'''
Created on 27 Nov 2024

@author: Giacomo
'''
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# ---- User Input Section ----
# Replace these arrays with your measurements.
m = np.array([24.769, 11.887, 8.374, 3.528])  # Masses [g]
sigma_m = np.full(m.shape, 0.001)  # Mass uncertainties [g]
d = np.array([18.25, 14.28, 12.69, 9.52])  # Diameters [mm]
sigma_d = np.full(d.shape, 0.01)  # Diameter uncertainties [mm]

# ---- Calculations ----
r = d / 2.0  # Radii [mm]
sigma_r = sigma_d / 2.0  # Radius uncertainties [mm]
V = 4.0 / 3.0 * np.pi * r**3.0  # Volumes [mm³]
sigma_V = V * 3.0 * sigma_d / d  # Volume uncertainties [mm³]

def line(x, m, q):
    """Modello lineare di fit."""
    return m * x + q

def power_law(x, norm, index):
    """Modello di tipo legge di potenza."""
    return norm * (x**index)

# ---- Graph: Mass vs Volume ----
plt.figure('Grafico massa-volume')
plt.errorbar(V, m, sigma_m, sigma_V, fmt='o')  # Data points with error bars
popt, pcov = curve_fit(line, V, m)  # Linear fit
m_hat, q_hat = popt
sigma_m_hat, sigma_q_hat = np.sqrt(pcov.diagonal())  # Fit uncertainties
print(m_hat, sigma_m_hat, q_hat, sigma_q_hat)  # Fit results
x = np.linspace(0., max(V) * 1.1, 100)  # Range for plot
plt.plot(x, line(x, m_hat, q_hat))  # Best-fit line
plt.xlabel('Volume [mm$^3$]')
plt.ylabel('Massa [g]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_volume.pdf')  # Save plot

# ---- Graph: Mass vs Radius ----
plt.figure('Grafico massa-raggio')
plt.errorbar(r, m, sigma_m, sigma_r, fmt='o')  # Data points with error bars
popt, pcov = curve_fit(power_law, r, m)  # Power-law fit
norm_hat, index_hat = popt
sigma_norm_hat, sigma_index_hat = np.sqrt(pcov.diagonal())  # Fit uncertainties
print(norm_hat, sigma_norm_hat, index_hat, sigma_index_hat)  # Fit results
x = np.linspace(min(r) * 0.9, max(r) * 1.1, 100)  # Range for plot
plt.plot(x, power_law(x, norm_hat, index_hat))  # Best-fit power-law line
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Raggio [mm]')
plt.ylabel('Massa [g]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_raggio.pdf')  # Save plot

plt.show()
