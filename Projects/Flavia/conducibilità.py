import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# ---- User Input Section ----
# Replace these arrays with your measurements.
macc = np.array([44.865,24.818,11.869,3.526,2.086])  # Masses [g]
sigma_macc = np.full(m.shape, 0.001)  # Mass uncertainties [g]
dacc = np.array([22.23,18.24,15.27,10.52,8])  # Diameters [mm]
sigma_dacc = np.full(d.shape, 0.01)  # Diameter uncertainties [mm]
Vacc = np.array([])
sigma_Vacc = np.array([])
mall = np.array([24.769, 11.887, 8.374, 3.528])  # Masses [g]
sigma_mall = np.full(m.shape, 0.001)  # Mass uncertainties [g]
dall = np.array([18.25, 14.28, 12.69, 9.52])  # Diameters [mm]
sigma_dall = np.full(d.shape, 0.01)  # Diameter uncertainties [mm]
Vall = np.array([])
sigma_Vall = np.array([])
mo = np.array([24.769, 11.887, 8.374, 3.528])  # Masses [g]
sigma_mo = np.full(m.shape, 0.001)  # Mass uncertainties [g]
do = np.array([18.25, 14.28, 12.69, 9.52])  # Diameters [mm]
sigma_d0 = np.full(d.shape, 0.01)  # Diameter uncertainties [mm]
Vo = np.array([])
sigma_Vo = np.array([])



def line(x, m, q):
    """Modello lineare di fit."""
    return m * x + q

def power_law(x, norm, index):
    """Modello di tipo legge di potenza."""
    return norm * (x**index)

# ---- Graph: Mass vs Volume ----
#acciaio
plt.figure('Grafico massa-volume')
plt.errorbar(Vacc, macc, sigma_macc, sigma_Vacc, fmt='o')  # Data points with error bars
popt, pcov = curve_fit(line, Vacc, macc)  # Linear fit
m_hat, q_hat = popt
sigma_macc_hat, sigma_qacc_hat = np.sqrt(pcov.diagonal())  # Fit uncertainties
print(macc_hat, sigma_macc_hat, qacc_hat, sigma_qacc_hat)  # Fit results
x = np.linspace(0., max(Vacc) * 1.1, 100)  # Range for plot
plt.plot(x, line(x, macc_hat, qacc_hat))  # Best-fit line
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