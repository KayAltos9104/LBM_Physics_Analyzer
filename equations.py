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
    return (n*R*T)/(V-n*b) - a*(n/V)*(n/V)

def vdw_pressure_molar (Vm, T, a, b, R=0.0821):
    n1 = R*T
    n2 = Vm-b
    n3 = n1/n2
    n4 = 1/Vm
    n5 = n4*n4
    n6 = n5*a
    return (R*T)/(Vm-b) - a*(1/Vm)*(1/Vm)