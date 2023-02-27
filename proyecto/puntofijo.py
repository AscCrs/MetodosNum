def fixed_point_iteration(g, x0, tolerance, max_iterations):
    """
    Implementa el método de iteración del punto fijo para encontrar una raíz de g(x)=x.

    Args:
        g (función): La función g(x) que se utiliza para la iteración del punto fijo.
        x0 (float): El valor inicial de x para comenzar la iteración.
        tolerance (float): La tolerancia de error para detener la iteración.
        max_iterations (int): El número máximo de iteraciones permitido.

    Returns:
        Tuple: Un par que contiene el valor de la raíz encontrada y el número de iteraciones realizadas.
    """
    x = x0
    for i in range(max_iterations):
        # Calcula la siguiente iteración
        x_next = g(x)

        # Calcula el error y verifica si se alcanzó la tolerancia
        error = abs(x_next - x)
        if error < tolerance:
            return x_next, i + 1  # Devuelve la raíz y el número de iteraciones realizadas

        # Muestra los resultados de esta iteración
        print(
            f"Iteración {i+1}: x={x:.6f}, g(x)={g(x):.6f}, error={error:.6f}")

        # Actualiza el valor de x para la próxima iteración
        x = x_next

    # Si se alcanza el número máximo de iteraciones, devuelve un mensaje de error
    raise ValueError(
        "El método de iteración del punto fijo no converge después de {} iteraciones.".format(max_iterations))


def g(x):
    return (1 - x**3)**(1/2)


root, num_iterations = fixed_point_iteration(
    g, x0=0.5, tolerance=1e-6, max_iterations=10000)
print(
    f"\nLa raíz encontrada es x={root:.6f} después de {num_iterations} iteraciones.")
