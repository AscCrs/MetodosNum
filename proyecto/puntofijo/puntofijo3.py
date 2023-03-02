# Algoritmo de punto fijo
# [a,b] intervalo de búsqueda
# error = tolera

import numpy as np


def puntofijo(gx, a, tolera, iteramax=15):
    i = 1  # iteración
    b = gx(a)
    tramo = abs(b-a)
    while (tramo >= tolera and i <= iteramax):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i + 1
    respuesta = b

    # Validar respuesta
    if (i >= iteramax):
        respuesta = np.nan
    return (respuesta)

# PROGRAMA ---------


# INGRESO
def fx(x): return (x ** 3) - (2 * x) - 5
def gx(x): return (2 ** 3) - 5


a = 1       # intervalo
b = 3
tolera = 0.001
iteramax = 15  # itera máximo
muestras = 51  # gráfico
tramos = 50

# PROCEDIMIENTO
respuesta = puntofijo(gx, a, tolera)

# SALIDA
print("La raiz aproximada esta en: ", respuesta)
