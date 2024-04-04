import math

# Young-Laplace Law
#fluid-fluid interface
def delta_pressure (sigma, teta, radius):
    return sigma*math.cos(math.radians(teta))/radius

def Radius (sigma, teta, delta_pressure):
    return sigma*math.cos(math.radians(teta))/delta_pressure

#Ideal Equation of State (EOS)
# P in atm
# V in L
# n in mols
# R in L*atm/mol/K
# T in K
def ideal_pressure (V, n, T, R=0.0821):
    return n*R*T/V

#Non-ideal Equation of State (EOS)
def vdw_pressure (V, n, T, a, b, R=0.0821):
    try:
        return (n*R*T)/(V-n*b) - a*(n/V)*(n/V)
    except:
        print(f'Деление на ноль: V={V}, b={b}')
def vdw_pressure_molar (Vm, T, a, b, R=0.0821):
    try:
        return (R*T)/(Vm-b) - a*(1/Vm)*(1/Vm)
    except:
        print(f'Деление на ноль: V={Vm}, b={b}')

# Psi function for One-Component Shan Chen
def psi (rho, psi0 = 4, rho0 = 200):
    return psi0*math.exp(-rho0/rho)

# Shan Chen equation of state
def shan_chen_pressure (G, rho=200):
    return rho/3 + (G/6)*psi(rho)*psi(rho)