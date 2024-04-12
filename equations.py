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
def psi2 (rho, rho0 = 200):
    return rho0*(1-math.exp(-rho/rho0))
def psi_vdW (rho, rho0 = 200):
    R=1
    b = 2/21
    a = 9/49
    T = 0.6
    G = -1


    try:
        #square = 6*rho/rho0 * (R*T/(1-b*rho/rho0) - a * rho/rho0 - 1/3)
        # По Юань
        square = 2 * ((rho / rho0) /(6*G)) * (R * T / (1 - b * rho / rho0) - a * rho / rho0 - 1 / 3)
        return math.sqrt(square)
    except:
        return None


# Shan Chen equation of state
def shan_chen_pressure (G, psi_func, rho=200):
    try:
        #return rho/3 + (G/6)*psi_func(rho)*psi_func(rho)
        # По Юань
        return rho / 3 + (3 * G ) * psi_func(rho) * psi_func(rho)
    except:
        return None