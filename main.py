import matplotlib.pyplot as plt
import numpy as np

import equations

x = np.arange(0.1, 0.5, 0.01)
y = np.vectorize(equations.vdw_pressure_molar)
plt.plot(x, y(x, T=373,a=3.592, b=0.4267))
#y = np.vectorize(equations.ideal_pressure)
#plt.plot(x, y(x, 1, 293))


plt.show()