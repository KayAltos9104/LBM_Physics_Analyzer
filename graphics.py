import matplotlib.pyplot as plt
import numpy as np




def plot(function, init_x=0, final_x=100, step_x=1):
    x = np.arange(init_x, final_x, step_x)
    y = np.vectorize(function)
    plt.plot(x, y(x))


def show_plot():
    plt.show()



