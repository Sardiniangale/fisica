'''
Created on 27 Nov 2024

@author: Giacomo
'''

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Corrected Data
masses = np.array([24.769, 11.887, 8.374, 3.528])  # Masses in grams
volumes = np.array([1, 2, 3, 4])  # Volumes in mm³ (corrected to match masses)

# ---- UNCERTAINTY ----
mass_uncertainties = np.full(masses.shape, 0.001)  # Mass uncertainty in grams
volume_uncertainties = np.full(volumes.shape, 0.01)  # Volume uncertainty in mm³

# ---- FITTING FUNCTIONS ----
def linear_model(x, slope, intercept):
    """Linear model: y = slope * x + intercept"""
    return slope * x + intercept

def power_law_model(x, norm, index):
    """Power-law model: y = norm * x^index"""
    return norm * (x**index)

# ---- PLOTTING AND ANALYSIS ----

# Mass vs. Volume Graph
plt.figure('Mass vs Volume')
plt.errorbar(volumes, masses, yerr=mass_uncertainties, xerr=volume_uncertainties, fmt='o', label='Data')

# Perform linear fit
popt, pcov = curve_fit(linear_model, volumes, masses)
slope, intercept = popt
slope_uncertainty, intercept_uncertainty = np.sqrt(np.diag(pcov))
print(f"Linear Fit Results:\nSlope (Density): {slope:.4f} ± {slope_uncertainty:.4f} g/mm³\nIntercept: {intercept:.4f} ± {intercept_uncertainty:.4f}")

# Plot linear fit
fit_volumes = np.linspace(0, max(volumes) * 1.1, 100)
plt.plot(fit_volumes, linear_model(fit_volumes, slope, intercept), label='Linear Fit', color='red')
plt.xlabel('Volume [mm³]')
plt.ylabel('Mass [g]')
plt.legend()
plt.grid(which='both', linestyle='dashed', color='gray')
plt.savefig('mass_vs_volume.pdf')

# Dummy radii data for Mass vs. Radius graph (correct as needed)
radii = np.array([1, 2, 3, 4])  # Radii in mm (example values)
radius_uncertainties = np.full(radii.shape, 0.1)  # Radius uncertainties in mm

# Mass vs. Radius Graph (Log-Log Scale)
plt.figure('Mass vs Radius')
plt.errorbar(radii, masses, yerr=mass_uncertainties, xerr=radius_uncertainties, fmt='o', label='Data')

# Perform power-law fit
popt, pcov = curve_fit(power_law_model, radii, masses)
norm, index = popt
norm_uncertainty, index_uncertainty = np.sqrt(np.diag(pcov))
print(f"Power-Law Fit Results:\nNorm: {norm:.4f} ± {norm_uncertainty:.4f}\nIndex: {index:.4f} ± {index_uncertainty:.4f}")

# Plot power-law fit
fit_radii = np.linspace(min(radii) * 0.9, max(radii) * 1.1, 100)
plt.plot(fit_radii, power_law_model(fit_radii, norm, index), label='Power-Law Fit', color='red')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Radius [mm]')
plt.ylabel('Mass [g]')
plt.legend()
plt.grid(which='both', linestyle='dashed', color='gray')
plt.savefig('mass_vs_radius.pdf')

# Show all plots
plt.show()

