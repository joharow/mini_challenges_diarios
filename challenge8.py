import random
import string

def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Garantizar que la contraseña contenga al menos un carácter de cada tipo
    mayuscula = random.choice(string.ascii_uppercase)
    minuscula = random.choice(string.ascii_lowercase)
    numero = random.choice(string.digits)
    simbolo = random.choice(string.punctuation)
    
    # Rellenar el resto de la contraseña
    contraseña = mayuscula + minuscula + numero + simbolo
    contraseña += ''.join(random.choice(caracteres) for _ in range(longitud - 4))
    
    # Mezclar los caracteres para evitar patrones predecibles
    contraseña = list(contraseña)
    random.shuffle(contraseña)
    
    return ''.join(contraseña)

if __name__ == "__main__":
    try:
        longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16): "))
        contraseña_segura = generar_contraseña(longitud)
        print(f"Contraseña generada: {contraseña_segura}")
    except ValueError as ve:
        print(ve)
