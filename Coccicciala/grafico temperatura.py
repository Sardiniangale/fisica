import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit 
tempA = np.array([30.54, 33.00, 35.33, 37.76, 39.92, 42.64, 45.62])
tempR = np.array([29.14, 30.98, 32.96, 34.64, 36.25, 38.24, 40.65])

sigma_tempA = np.full(tempA.shape, 0.01)
sigma_tempR = np.full(tempR.shape, 0.01)

distA=0.048 #distanza tra i buchi in cui abbiamo preso la temperatura
distR=0.064

delta_lA = np.arange(0, 0.3, 0.048)
delta_lR = np.arange(0, 0.4, 0.064)

sigma_lA = np.full(lA.shape, 0.001)
sigma_lR = np.full(lR.shape, 0.001)

diamA = 0.02520
diamR = 0.02520

sigma_diamA = 0.00005
sigma_diamA = 0.00005
print(lA, lR)
def line(delta_lA, m, q):
    return m * delta_lA + q 
plt.figure("grafico temperatura in base alla posizione")
plt.errorbar(delta_lA, tempA, sigma_tempA, sigma_lA, fmt="o")
popt, pcov = curve_fit(line, delta_lA, tempA, 
