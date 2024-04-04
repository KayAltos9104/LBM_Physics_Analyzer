import matplotlib.pyplot as plt
import numpy as np

import equations


# Кривые для CO2
def show_co2_isotherms():
    x = np.arange(0.05, 0.5, 0.001)
    y = np.vectorize(equations.vdw_pressure)

    for T in range(200, 450, 30):
        plt.plot(x, y(x, n=1, T=T, a=3.59, b=0.04267), label=f'T={T}')
    plt.legend()
    plt.xlabel('Vm, L')
    plt.ylabel('p, atm')
    plt.show()


# Кривые rho-V для Шань-Ченя
def show_shan_chen_density_curves():
    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
            }
    density = np.arange(1, 1000, 0.01)
    pressure = np.vectorize(equations.shan_chen_pressure)
    for G in range(-144, -47, 12):
        # plt.text(1000, 200 - 0.65*abs(G), f'G={G}', font)
        plt.plot(density, pressure(G, density), label=f'G={G}')
    plt.xlabel('Density, [mass unit]/[lattice unit]^2')
    plt.ylabel('p, [mass unit]/[time step]^2')
    plt.legend()
    plt.show()


def main():
    show_co2_isotherms()
    show_shan_chen_density_curves()


if __name__ == '__main__':
    main()
