'''
Created on 16 Dec 2024

@author: Giacomo
'''
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Dati---mettete le vostre misure!
# Qui potete anche leggere i dati da file, usando il metodo np.loadtxt(),
# se lo trovate comodo.
d = np.array([47.5, 37.5, 27.5, 17.5, 7.5, 2.5, 12.5, 22.5, 32.5, 42.5])
sigma_d = np.full(d.shape, 0.1)
T = np.array([1.536, 1.456, 1.452, 1.556, 2.166, 3.646, 1.758, 1.494, 1.482, 1.502])
l = (105)
sigma_T = np.array([0.02586503431, 0.007348469228, 0.02260530911, 0.013, 0.1546415209, 0.06541406577, 0.07287660804, 0.02244994432, 0.0514392846, 0.02619160171])

# Definizione dell’accelerazione di gravita‘.
g = 981

def period_model(d, l):
    return 2.0 * np.pi * np.sqrt((l**2.0 / 12.0 + d**2.0) / (g * d))

plt.figure('Periodo')
# Scatter plot dei dati.
plt.errorbar(d, T, sigma_T, sigma_d, fmt='o')
# Fit---notate che questo e‘ un fit ad un solo parametro.
popt, pcov = curve_fit(period_model, d, T, sigma=sigma_T)
l_hat = popt[0]
sigma_l = np.sqrt(pcov[0, 0])
# Confrontate i parametri di best fit con la vostra misura diretta!
print(l_hat, sigma_l)
# Grafico del modello di best-fit.
x = np.linspace(0.5, 50, 100)
plt.plot(x, period_model(x, l_hat))
plt.xlabel('d [cm]')
plt.ylabel('Periodo [s]')
plt.grid(which='both', ls='dashed', color='gray')
plt.savefig('massa_raggio.pdf')
plt.show()