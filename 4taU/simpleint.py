import numpy as np
from scipy.integrate import fixed_quad

"""
! Para todas las funciones, los parametros que reciben son:

* f: es la función que se desea integrar.
* a: es el límite inferior del intervalo de integración.
* b: es el límite superior del intervalo de integración.
* n: es el número de subintervalos que se desean utilizar en la integración.
"""

# Definición de la regla del trapecio
def trapezoidal_integration(f, a, b, n):
    h = (b-a)/n  # calcula el ancho de cada subintervalo
    x = np.linspace(a, b, n+1)  # genera los puntos equidistantes a lo largo del intervalo
    y = f(x)  # evalúa la función en los puntos x generados
    y_left = y[:-1]  # guarda los valores de la función en la izquierda de cada subintervalo
    y_right = y[1:]  # guarda los valores de la función en la derecha de cada subintervalo
    return (h/2) * np.sum(y_left + y_right)  # aplica la fórmula de la regla del trapecio y retorna el resultado

# Definición de la regla de Simpson
def simpsons_integration(f, a, b, n):
    # Calcula el tamaño del intervalo
    h = (b-a)/n
    # Genera puntos equidistantes en el intervalo
    x = np.linspace(a, b, n+1)
    # Calcula los valores de la función en los puntos generados
    y = f(x)
    # Selecciona los valores de la función en los extremos izquierdo y derecho del intervalo
    y_left = y[:-2:2]
    y_right = y[2::2]
    # Selecciona los valores de la función en el punto medio del intervalo
    y_middle = y[1:-1:2]
    # Aplica la regla de Simpson
    return (h/3) * np.sum(y_left + 4*y_middle + y_right)

# Definición del método de cuadratura de Gauss
def gaussian_quadrature_integration(f, a, b, n):
    # Obtiene las abscisas (x) y pesos (w) para el método de cuadratura de Gauss
    x, w = gaussian_quadrature_weights(n)
    # Ajusta los pesos y abscisas al intervalo de integración [a,b]
    x_adjusted = 0.5*(b-a)*x + 0.5*(b+a)
    w_adjusted = 0.5*(b-a)*w
    # Calcula la aproximación de la integral utilizando los pesos y abscisas ajustados
    integral_approx = np.sum(w_adjusted * f(x_adjusted))
    # Devuelve la aproximación de la integral
    return integral_approx

"""
La función gaussian_quadrature_weights recibe un entero n que indica el número de puntos 
de integración deseado. En función de este valor, se determinan las abscisas y pesos 
correspondientes para la cuadratura gaussiana.

Si n es igual a 1, se devuelve un único punto y su peso, 0 y 2 respectivamente, 
ya que la cuadratura gaussiana es exacta para funciones polinómicas de grado menor o igual a 1.

Si n es igual a 2, se devuelven dos puntos y pesos iguales, correspondientes a 
la cuadratura gaussiana en el intervalo [-1, 1]. Estos valores se eligen de tal 
manera que la cuadratura gaussiana sea exacta para funciones polinómicas de grado 
menor o igual a 3.

Si n es igual a 3, se devuelven tres puntos y pesos correspondientes a la cuadratura 
gaussiana en el intervalo [-1, 1]. Estos valores se eligen de tal manera que la cuadratura 
gaussiana sea exacta para funciones polinómicas de grado menor o igual a 5.

Si n es igual a 4, se devuelven cuatro puntos y pesos correspondientes a la cuadratura 
gaussiana en el intervalo [-1, 1]. Estos valores se eligen de tal manera que la cuadratura 
gaussiana sea exacta para funciones polinómicas de grado menor o igual a 7.

Si n es mayor o igual a 5, se utilizan las abscisas y pesos obtenidos a partir de la 
fórmula recursiva de Legendre, que genera los valores para la cuadratura gaussiana a 
partir de los polinomios de Legendre.

Si n no es un valor válido, se genera un error ValueError.

La función devuelve dos arrays de numpy, uno con las abscisas y otro con los pesos 
correspondientes para la cuadratura gaussiana de n puntos.
"""
def gaussian_quadrature_weights(n):
    # Definimos la cuadratura para distintos valores de n
    if n == 1:
        x = np.array([0.0])
        w = np.array([2.0])
    elif n == 2:
        x = np.array([-np.sqrt(1/3), np.sqrt(1/3)])
        w = np.array([1.0, 1.0])
    elif n == 3:
        x = np.array([-np.sqrt(3/5), 0.0, np.sqrt(3/5)])
        w = np.array([5/9, 8/9, 5/9])
    elif n == 4:
        x = np.array([-np.sqrt((3+2*np.sqrt(6/5))/7), -np.sqrt((3-2*np.sqrt(6/5))/7),
                      np.sqrt((3-2*np.sqrt(6/5))/7), np.sqrt((3+2*np.sqrt(6/5))/7)])
        w = np.array([(18-np.sqrt(30))/36, (18+np.sqrt(30))/36, (18+np.sqrt(30))/36, (18-np.sqrt(30))/36])
    elif n >= 5:
        # Si n es mayor o igual a 5, usar la fórmula recursiva de Legendre-Gauss
        x, w = np.polynomial.legendre.leggauss(n)
    else:
        # Si n no es un valor válido, lanzar una excepción
        raise ValueError("Número de puntos de integración no válido")
    # Devolvemos los pesos y abscisas
    return x, w


# Definición de la función a integrar
def f(x):
    return x**3 - 2*x**2 + 3*x - 4

if __name__ == "__main__":
    # Límites de integración
    a, b = 1, 4  # Intervalo de integración
    n = 20  # Número de puntos de integración

    # Aproximación de la integral utilizando la regla del trapecio
    trapezoidal_result = trapezoidal_integration(f, a, b, n)
    print("Resultado de integración por el método del Trapecio:", trapezoidal_result)

    # Aproximación de la integral utilizando la regla de Simpson
    simpsons_result = simpsons_integration(f, a, b, n)
    print("Resultado de integración por la regla de Simpson's:", simpsons_result)

    # Aproximación de la integral utilizando el método de cuadratura de Gauss
    gaussian_quadrature_result = gaussian_quadrature_integration(f, a, b, n)
    print("Resultado de integración por el método de Caudratura de Gauss:", gaussian_quadrature_result)