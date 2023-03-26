import numpy as np

"""
Función para realizar la integración mediante el método del trapecio

Parámetros:
f: función a integrar
a: límite inferior del intervalo
b: límite superior del intervalo
n: número de subintervalos
"""
def trapezoidal_integration(f, a, b, n):
    # Calcula el tamaño del subintervalo
    h = (b-a)/n
    # Genera un arreglo de puntos equidistantes en el intervalo [a,b]
    x = np.linspace(a, b, n+1)
    # Calcula los valores de la función en los puntos equidistantes
    y = f(x)
    # Toma todos los valores de la función excepto el último
    y_left = y[:-1]
    # Toma todos los valores de la función excepto el primero
    y_right = y[1:]
    # Realiza la integración por el método del trapecio
    return (h/2)*np.sum(y_left + y_right)

"""
Función para realizar la integración mediante la regla de Simpson

Parámetros:
f: función a integrar
a: límite inferior del intervalo
b: límite superior del intervalo
n: número de subintervalos
"""
def simpsons_integration(f, a, b, n):
    # Ajusta el número de subintervalos para que sea par
    if n % 2 != 0:
        n += 1
    # Calcula el tamaño del subintervalo
    h = (b - a) / n
    # Genera un arreglo de puntos equidistantes en el intervalo [a,b]
    x = np.linspace(a, b, n+1)
    # Calcula los valores de la función en los puntos equidistantes
    y = f(x)
    # Toma los valores de la función con índices pares
    y_left = y[:-2:2]
    # Toma los valores de la función con índices impares
    y_middle = y[1::2]
    # Toma los valores de la función con índices pares
    y_right = y[2::2]
    # Realiza la integración por la regla de Simpson
    return (h/3) * np.sum(y_left + 4*y_middle + y_right)

"""
Función para realizar la integración mediante el método de Monte Carlo

Parámetros:
f: función a integrar
a: límite inferior del intervalo
b: límite superior del intervalo
n: número de subintervalos
"""
def monte_carlo_integration(f, a, b, n):
    # Genera n puntos aleatorios en el intervalo [a,b]
    x = np.random.uniform(a, b, n)
    # Genera n puntos aleatorios en el intervalo [0, f(b)]
    y = np.random.uniform(0, np.max(f(x)), n)
    # Calcula el área de la caja que contiene a la función
    area_box = (b-a)*np.max(f(x))
    # Calcula el área debajo de la curva mediante el método de Monte Carlo
    area_under_curve = area_box*np.sum(y < f(x))
    return area_under_curve/n

"""
Función para realizar la integración mediante el método de cuadratura Gaussiana

Parámetros:
f: función a integrar
a: límite inferior del intervalo
b: límite superior del intervalo
n: número de subintervalos
"""
def gaussian_quadrature_integration(f, a, b, n):
    # Calcula las raíces y los pesos de los polinomios de Legendre
    x, w = np.polynomial.legendre.leggauss(n)
    # Transforma las raíces a la escala del intervalo [a,b]
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    # Transforma los pesos a la escala del intervalo [a,b]
    wp = 0.5*(b-a)*w
    # Realiza la integración por el método de cuadratura Gaussiana
    return np.sum(wp*f(xp))

"""
Función para realizar la integración mediante el método del rectangulo

Parámetros:
f: función a integrar
a: límite inferior del intervalo
b: límite superior del intervalo
n: número de subintervalos
"""
def rectangle_integration(f, a, b, n):
    # Cálculo del tamaño de los subintervalos
    h = (b-a)/n
    # Generación de los puntos x donde se evaluará la función
    x = np.linspace(a, b, n+1)
    # Evaluación de la función f en los puntos x, excepto el último
    y = f(x[:-1])
    # Cálculo de la aproximación de la integral mediante la regla del rectángulo
    return h*np.sum(y)

# Definición de la función a integrar sen(x)
def f(x):
    return np.sin(x)

if __name__ == '__main__':
    # Definición de las variables
    a, b = 0, np.pi/2
    n = 10
    
    trapezoidal_result = trapezoidal_integration(f, a, b, n)
    print("Resultado de integración por el método del trapecio:", trapezoidal_result)
    
    simpsons_result = simpsons_integration(f, a, b, n)
    print("Resultado de integración por el método de Simpson's:", simpsons_result)
    
    monte_carlo_result = monte_carlo_integration(f, a, b, n)
    print("Resultado de integración por el método de Monte Carlo:", monte_carlo_result)
    
    gaussian_quadrature_result = gaussian_quadrature_integration(f, a, b, n)
    print("Resultado de integración por el método de Cuadratura Gaussiana:", gaussian_quadrature_result)
    
    rectangle_result = rectangle_integration(f, a, b, n)
    print("Resultado de integración por el método del Rectangulo:", rectangle_result)