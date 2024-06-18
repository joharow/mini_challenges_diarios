def celsius_a_fahrenheit(celsius):
    """
    Esta función convierte una temperatura dada en grados Celsius a grados Fahrenheit.
    
    Parámetros:
    celsius (float): La temperatura en grados Celsius con decimales.

    Retorna:
    La temperatura convertida a grados Fahrenheit.
    """
    # Aplicar la fórmula de conversión de Celsius a Fahrenheit
    return celsius * 9 / 5 + 32

# Solicitar al usuario que introduzca la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Llamar a la función de conversión y almacenar el resultado en una variable
fahrenheit = celsius_a_fahrenheit(celsius)

# Imprimir el resultado de la conversión
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
