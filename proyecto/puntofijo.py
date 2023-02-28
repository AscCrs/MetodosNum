import math


def fixed_point_iteration(x0, tol, max_iter):
    """
    Método de punto fijo para resolver la ecuación x = cos(x)
    :param x0: Valor inicial
    :param tol: Tolerancia del error
    :param max_iter: Número máximo de iteraciones
    :return: Solución aproximada de la ecuación x = cos(x)
    """
    print("Iteración 0: x = ", x0)
    for i in range(1, max_iter+1):
        x1 = math.cos(x0)
        error = abs(x1 - x0)
        print(f"Iteración {i}: x = {x1}, error = {error}")
        if error < tol:
            print(
                f"\nSolución encontrada después de {i} iteraciones: x = {x1}")
            return x1
        x0 = x1
    print("\nNúmero máximo de iteraciones alcanzado.")
    return None


x0 = 1.0
tol = 1e-6
max_iter = 100

fixed_point_iteration(x0, tol, max_iter)
