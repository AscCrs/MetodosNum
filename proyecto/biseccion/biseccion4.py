import math

tol = 1e-6

# Limite inferior: 0
# Limite superior: 1
# Esperado: 0.6190609931945801


def f(x):
    return (math.exp(x)) - (3 * x)


def biseccion(min, max):
    med = (min + max) / 2
    if (max - min < tol):
        return med
    elif (f(min) * f(med) < 0):
        return biseccion(min, med)
    else:
        return biseccion(med, max)


limin = float(input("Ingrese el limite inferior: "))
limax = float(input("Ingrese el limite superior: "))

print("Raíz aproximada en: " + str(biseccion(limin, limax)))
