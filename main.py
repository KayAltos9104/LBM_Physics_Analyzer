import matplotlib.pyplot as plt
import numpy as np

import equations
# Кривые для CO2
x = np.arange(0.05, 0.5, 0.001)
y = np.vectorize(equations.vdw_pressure)

for T in range(200, 500, 20):
    plt.plot(x, y(x, n=1, T=T, a=3.59, b=0.04267))
plt.show()
