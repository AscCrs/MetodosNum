import math

tol = 1e-6

# Limite inferior: 1
# LImite superior: 3
# Esperado: 2.0945515632629395


def f(x):
    return (x ** 3) - (2 * x) - 5


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
