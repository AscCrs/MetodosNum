def newton_raphson(f, df, x0, eps=1e-6, max_iter=100):
    """
    Encuentra una raíz de la función f(x) utilizando el método de
    Newton-Raphson.

    Parámetros:
    f: función a la cual se le quiere encontrar la raíz.
    df: derivada de la función f.
    x0: aproximación inicial.
    eps: tolerancia de error.
    max_iter: número máximo de iteraciones.

    Retorna:
    x: aproximación de la raíz.
    """
    for i in range(max_iter):
        fx0 = f(x0)
        dfx0 = df(x0)
        x1 = x0 - fx0 / dfx0
        print(f"Iteración {i}: x = {x1}")
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1
    print("Error: se alcanzó el número máximo de iteraciones.")
    return None

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x0 = 1.5
eps = 1e-6
max_iter = 100

def newton_raphson(f, df, x0, eps, max_iter):
    for i in range(max_iter):
        fx0 = f(x0)
        dfx0 = df(x0)
        x1 = x0 - fx0 / dfx0
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1
    print("Error: se alcanzó el número máximo de iteraciones.")
    return None

x = newton_raphson(f, df, x0, eps, max_iter)
print("La raíz es:", x)
