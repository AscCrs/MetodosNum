import math

tol = 1e-6

def f (x):
    return 4 * math.pow(x, 3) - 6 * math.pow(x, 2) + 7 * x - 2.3

def biseccion(min, max):
    med = (min + max) / 2
    if (max - min < tol):
        return med
    elif (f(min) * f(med) < 0):
        return biseccion (min, med)
    else: 
        return biseccion (med, max)

limin = float(input("Ingrese el limite inferior: "))
limax = float(input("Ingrese el limite superior: "))

print("Raíz aproximada en: " + str(biseccion(limin, limax)))
