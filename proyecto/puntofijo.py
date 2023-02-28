import math


def f(x):
    return math.cos(x)


def g(x):
    return f(x) + x


def punto_fijo(g, x0, tol, max_iter):
    """
    Implementación del método de punto fijo
    :param g: Función g(x) a evaluar
    :param x0: Valor inicial
    :param tol: Tolerancia de error
    :param max_iter: Número máximo de iteraciones
    :return: Aproximación de la solución de la ecuación g(x) = x
    """
    x = x0
    iter = 0
    error = tol + 1
    print("Iteración\t\t x\t\t\t\t error")
    print("-"*50)
    while error > tol and iter < max_iter:
        x_ant = x
        x = g(x_ant)
        iter += 1
        error = abs(x - x_ant)
        print("{:d}\t\t\t {:.10f}\t\t {:.10f}".format(iter, x, error))
    print("-"*50)
    if iter == max_iter:
        print("El método de punto fijo no converge en {} iteraciones".format(max_iter))
        return None
    else:
        print("La aproximación de la solución es: {:.10f}".format(x))
        return x


# Ejemplo de uso
punto_fijo(g, 1, 1e-5, 100)
