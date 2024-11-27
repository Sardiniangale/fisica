'''
Created on 27 Nov 2024

@author: Giacomo
'''


import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


masses = np.array([24.769, 11.887, 8.374, 3.528])  # Masses in grams
diameters = np.array([18.25, 14.28, 12.69, 9.52])  # Diameters in mm

# Measurement uncertainties
mass_uncertainties = np.full(masses.shape, 0.001)  # Mass uncertainty in grams
diameter_uncertainties = np.full(diameters.shape, 0.01)  # Diameter uncertainty in mm

# ---- CALCULATIONS ----
# Calculate radii and their uncertainties
radii = diameters / 2.0
radius_uncertainties = diameter_uncertainties / 2.0

# Calculate volumes and their uncertainties using propagation of errors
volumes = (4.0 / 3.0) * np.pi * radii**3
volume_uncertainties = volumes * 3.0 * diameter_uncertainties / diameters

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
