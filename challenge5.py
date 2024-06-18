
def crear_diccionario(claves, valores):
    if len(claves) != len(valores):
        raise ValueError("Las listas de claves y valores deben tener la misma longitud")
    
    diccionario = dict(zip(claves, valores))
    return diccionario

# Ejemplo de uso
animales = ['gato', 'perro', 'vaca', 'oveja', 'pato']
sonidos = ['miau', 'guau', 'muuu', 'beee', 'cuac']

diccionario_animales = crear_diccionario(animales, sonidos)
print(diccionario_animales)
