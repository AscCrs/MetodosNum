import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 3*x**2 + 3*x - 1

def metodo_grafico(f, x0, x1, eps, max_iter):
    for i in range(max_iter):
        x = np.linspace(x0, x1, 100)
        y = f(x)
        plt.plot(x, y)
        plt.axhline(y=0, color='r', linestyle='-')
        plt.axvline(x=x0, color='g', linestyle='-')
        plt.axvline(x=x1, color='g', linestyle='-')
        plt.show()
        if abs(x1 - x0) < eps:
            return (x0 + x1) / 2
        x0 = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
        x1 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    print("Error: se alcanzó el número máximo de iteraciones.")
    return None

x0 = 0
x1 = 2
eps = 1e-6
max_iter = 10

x = metodo_grafico(f, x0, x1, eps, max_iter)
print("La raíz es:", x)
