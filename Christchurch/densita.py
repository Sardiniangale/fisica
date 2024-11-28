'''
Created on 27 Nov 2024

@author: Giacomo
'''

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# ---- DATA INPUT ----
materials = {
    "Material A": {
        "masses": np.array([]),
        "volumes": np.array(]),
        "mass_uncertainties": np.array([0,01]),  
        "volume_uncertainties": np.array([4.4816524592089,3.01723347681125,2.11464428888324,1.00366950579773,0.58041579655495])  
 },
    "Material B": {
        "masses": np.array([]),
        "volumes": np.array([]),
        "mass_uncertainties": np.array([0,01]),  
        "volume_uncertainties": np.array([5.65212195704233,2.80162656269473,1.38105892221567,4.29384324662944,2.73065638846688,])  
    }, 
    "Material C": {
        "masses": np.array([]),
        "volumes": np.array([]),
        "mass_uncertainties": np.array([0,01]),  
        "volume_uncertainties": np.array([1.97566042733464,5.9352107253293,1.6108751890243,3.4845439,5.65212195704233])  
    }
}


# ---- FITTING FUNCTION ----
def linear_model(x, slope, intercept):
    """Linear model: y = slope * x + intercept"""
    return slope * x + intercept

# ---- PLOTTING AND ANALYSIS ----
plt.figure('Mass vs Volume')

for material, data in materials.items():
    masses = data["masses"]
    volumes = data["volumes"]
    mass_uncertainties = data["mass_uncertainties"]
    volume_uncertainties = data["volume_uncertainties"]

    # Plot data with individual error bars
    plt.errorbar(
        volumes, masses, 
        yerr=mass_uncertainties, xerr=volume_uncertainties, 
        fmt='o', label=f'{material} Data'
    )

    # Perform linear fit
    popt, pcov = curve_fit(
        linear_model, volumes, masses, 
        sigma=mass_uncertainties,  # Weight fit by mass uncertainties
        absolute_sigma=True  # Treat uncertainties as absolute
    )
    slope, intercept = popt
    slope_uncertainty, intercept_uncertainty = np.sqrt(np.diag(pcov))
    print(f"{material} Linear Fit Results:")
    print(f"  Slope (Density): {slope:.4f} ± {slope_uncertainty:.4f} g/cm³")
    print(f"  Intercept: {intercept:.4f} ± {intercept_uncertainty:.4f}\n")

    # Generate and plot the linear fit line
    fit_volumes = np.linspace(0, max(volumes) * 1.1, 100)
    plt.plot(
        fit_volumes, linear_model(fit_volumes, slope, intercept), 
        label=f'{material} Fit', linestyle='--'
    )

# Add labels, legend, and grid
plt.xlabel('Volume [cm³]')
plt.ylabel('Mass [g]')
plt.legend()
plt.grid(which='both', linestyle='dashed', color='gray')
plt.title('Mass vs Volume for Different Materials with Individual Uncertainties')
plt.savefig('mass_vs_volume_multimaterial_individual_uncertainties.pdf')



#radii = np.array([1, 2, 3, 4])  # Radii in cm (example values)
#radius_uncertainties = np.full(radii.shape, 0.1)  # Radius uncertainties in cm

# Mass vs. Radius Graph (Log-Log Scale)
#plt.figure('Mass vs Radius')
#plt.errorbar(radii, masses, yerr=mass_uncertainties, xerr=radius_uncertainties, fmt='o', label='Data')

# Perform power-law fit
#popt, pcov = curve_fit(power_law_model, radii, masses)
#norm, index = popt
#norm_uncertainty, index_uncertainty = np.sqrt(np.diag(pcov))
#print(f"Power-Law Fit Results:\nNorm: {norm:.4f} ± {norm_uncertainty:.4f}\nIndex: {index:.4f} ± {index_uncertainty:.4f}")

# Plot power-law fit
#fit_radii = np.linspace(min(radii) * 0.9, max(radii) * 1.1, 100)
#plt.plot(fit_radii, power_law_model(fit_radii, norm, index), label='Power-Law Fit', color='red')
#plt.xscale('log')
#plt.yscale('log')
#plt.xlabel('Radius [cm]')
#plt.ylabel('Mass [g]')
#plt.legend()
#plt.grid(which='both', linestyle='dashed', color='gray')
#plt.savefig('mass_vs_radius.pdf')

# Show all plots
plt.show()

