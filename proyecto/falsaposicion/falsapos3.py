import math


def falsa_posicion(f, a, b, eps=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función f en el intervalo [a, b]
    utilizando el método de falsa posición.

    Parámetros:
    f: función a la que se le busca la raíz.
    a, b: límites del intervalo en el que se busca la raíz.
    eps: tolerancia de error.
    max_iter: número máximo de iteraciones.

    Retorna:
    x: aproximación de la raíz.
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        print("Error: la función no cambia de signo en el intervalo.")
        return None
    for i in range(max_iter):
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        print(f"Iteración {i}: x = {x}, f(x) = {fx}")
        if abs(fx) < eps:
            return x
        if fx * fa < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx
    print("Error: se alcanzó el número máximo de iteraciones.")
    return None


def f(x):
    return math.cos(x) - x


a = 0  # Limite inferior
b = 1  # Limite superior
eps = 1e-6
max_iter = 100
x = falsa_posicion(f, a, b, eps, max_iter)
if x is not None:
    # Esperado: 0.739085
    print(f"La raíz aproximada es {x:.6f}")
else:
    print("No se ha encontrado la raiz")
