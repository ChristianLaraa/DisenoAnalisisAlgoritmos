def se_puede_formar(n):
    # Crear una lista para almacenar si es posible formar un número i
    posible = [False] * (n + 1)

    # Base case: el número 0 siempre se puede formar (no seleccionar ningún paquete)
    posible[0] = True

    # Recorrer todos los números desde 1 hasta n
    for i in range(1, n + 1):
        # Verificar si se puede formar el número actual usando un paquete de 5, 8 o 24
        if i >= 5 and posible[i - 5]:
            posible[i] = True
        if i >= 8 and posible[i - 8]:
            posible[i] = True
        if i >= 24 and posible[i - 24]:
            posible[i] = True

    return posible[n]


# Ejemplo de uso:
n = 10
if se_puede_formar(n):
    print(f"Es posible formar el número {n} usando paquetes de 5, 8 y 24 plumas.")
else:
    print(f"No es posible formar el número {n} usando paquetes de 5, 8 y 24 plumas.")