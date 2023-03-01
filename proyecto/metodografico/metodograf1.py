import matplotlib.pyplot as plt
import numpy as np

# Definimos la función a resolver


def f(x):
    return x**2 + 2*x - 5


# Definimos el intervalo donde buscamos la solución
a = -4
b = 2

# Generamos un arreglo de valores para x
x = np.linspace(a, b, 100)

# Evaluamos la función en cada valor de x
y = f(x)

# Graficamos la función
plt.plot(x, y)

# Agregamos los ejes x e y
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)

# Agregamos etiquetas a los ejes
plt.xlabel('x')
plt.ylabel('y')

# Agregamos un título al gráfico
plt.title('Método gráfico')

# Definimos un valor inicial para x
x0 = -3

# Definimos la tolerancia del método
tolerancia = 1e-6

# Iteramos hasta encontrar la solución o hasta llegar al límite máximo de iteraciones
max_iteraciones = 100
iteracion = 0
while iteracion < max_iteraciones:
    # Evaluamos la función en el valor actual de x
    y0 = f(x0)

    # Graficamos el punto actual en la función
    plt.plot(x0, y0, 'ro')

    # Si encontramos una solución dentro de la tolerancia, detenemos la iteración
    if abs(y0) < tolerancia:
        break

    # Calculamos el siguiente valor de x como la intersección con el eje x
    x1 = x0 - y0 / (f(x0 + tolerancia) - f(x0)) * tolerancia

    # Graficamos la línea entre los dos puntos
    plt.plot([x0, x1], [y0, 0], 'g--')

    # Actualizamos el valor de x para la siguiente iteración
    x0 = x1

    # Incrementamos el contador de iteraciones
    iteracion += 1

# Mostramos el gráfico
plt.show()

# Imprimimos la solución encontrada
print(f"La solución es x = {x0}")
