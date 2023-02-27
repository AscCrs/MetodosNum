import math

def punto_fijo(g, x0, eps=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función g(x) = x utilizando el método
    del punto fijo.

    Parámetros:
    g: función de punto fijo.
    x0: aproximación inicial.
    eps: tolerancia de error.
    max_iter: número máximo de iteraciones.

    Retorna:
    x: aproximación de la raíz.
    """
    for i in range(max_iter):
        x1 = g(x0)
        print(f"Iteración {i}: x = {x1}")
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1
    print("Error: se alcanzó el número máximo de iteraciones.")
    return None

def g(x):
    return (math.e**x) - 2 - x

x0 = 0
eps = 1e-6
max_iter = 100  

x = punto_fijo(g, x0, eps, max_iter)

if x is not None:
    print(f"La raíz aproximada es {x:.6f}")
else:
    print("No se encontró la raíz.")
