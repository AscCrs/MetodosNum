def secante(f, x0, x1, tol, maxiter):
    """
    Función para encontrar una raíz de la función f(x) utilizando el método de la secante.

    Parámetros:
    f: función a la cual se busca encontrar la raíz.
    x0: valor inicial para x0.
    x1: valor inicial para x1.
    tol: tolerancia para el error.
    maxiter: número máximo de iteraciones.

    Retorna:
    x1: aproximación de la raíz de f(x).
    """

    # Inicializar los valores de las iteraciones.
    f0, f1 = f(x0), f(x1)
    i = 0

    # Realizar las iteraciones hasta que se alcance la tolerancia o el número máximo de iteraciones.
    while abs(f1) > tol and i < maxiter:
        # Calcular la nueva aproximación utilizando la fórmula de la secante.
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        # Actualizar los valores de las funciones y de x0 y x1 para la siguiente iteración.
        f0, f1 = f1, f(x2)
        x0, x1 = x1, x2

        # Incrementar el contador de iteraciones.
        i += 1

    return x1


def f(x):
    return x**3 - 2*x - 5


x0 = 2
x1 = 3
tol = 1e-6
maxiter = 100

raiz = secante(f, x0, x1, tol, maxiter)

print("La raíz de f(x) es:", raiz)
