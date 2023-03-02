import math


def punto_fijo(f, x0, tolerancia, max_iter):
    """
    Encuentra una aproximación del punto fijo de la función f(x) utilizando el método de iteración de punto fijo.

    Args:
        f (function): La función a encontrar el punto fijo.
        x0 (float): Suposición inicial.
        tolerancia (float): La tolerancia para la convergencia.
        max_iter (int): Número máximo de iteraciones permitidas.

    Returns:
        float: Aproximación del punto fijo de la función.
        str: Mensaje de error si el método no converge dentro del número máximo de iteraciones permitidas.
    """
    x_ant = x0
    for i in range(max_iter):
        x_act = f(x_ant)
        if abs(x_act - x_ant) < tolerancia:
            return x_act
        x_ant = x_act
    return "El método no converge después de {} iteraciones.".format(max_iter)


def f(x):
    return x - math.tan(x)


x0 = 1
tolerancia = 0.0001
max_iter = 100

resultado = punto_fijo(f, x0, tolerancia, max_iter)

if isinstance(resultado, float):
    print("El punto fijo es: {}".format(resultado))
else:
    print(resultado)
