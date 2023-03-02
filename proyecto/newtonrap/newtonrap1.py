def newton_raphson(f, df, x0, tol, max_iter):
    """
    Método de Newton-Raphson para encontrar las raíces de una función.
    Parámetros:
        - f: función a la cual se le buscarán las raíces.
        - df: derivada de la función f.
        - x0: valor inicial para comenzar la búsqueda de la raíz.
        - tol: tolerancia para considerar que se ha encontrado la raíz.
        - max_iter: número máximo de iteraciones permitidas.
    Retorna:
        - La raíz encontrada.
    """
    i = 0
    xi = x0
    error = abs(f(xi))
    print("Iteración\tRaíz\t\tError")
    print("-" * 40)
    print(f"{i}\t\t{xi:.10f}\t{error:.10f}")

    while error > tol and i < max_iter:
        xi -= f(xi) / df(xi)
        i += 1
        error = abs(f(xi))
        print(f"{i}\t\t{xi:.10f}\t{error:.10f}")

    if i == max_iter:
        print(
            f"\nSe alcanzó el número máximo de iteraciones ({max_iter}) sin encontrar una raíz con tolerancia {tol}")
    else:
        print(
            f"\nSe encontró una raíz en {xi:.10f} después de {i} iteraciones con tolerancia {tol}")

    return xi


def f(x):
    #     return 4 * math.pow(x, 3) - 6 * math.pow(x, 2) + 7 * x - 2.3
    return (4 * x ** 3) - (6 * x ** 2) + (7 * x) - 2.3


def df(x):
    return (12 * x ** 2) - (12 * x) + 7


x0 = 0  # Valor inicial
tol = 1e-6
max_iter = 20
#

newton_raphson(f, df, x0, tol, max_iter)
