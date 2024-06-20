import random

def obtener_eleccion_computadora():
    opciones = ['piedra', 'papel', 'tijeras']
    return random.choice(opciones)

def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijeras: ").lower()
    while eleccion not in ['piedra', 'papel', 'tijeras']:
        eleccion = input("Elección inválida. Elige piedra, papel o tijeras: ").lower()
    return eleccion

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == 'piedra' and computadora == 'tijeras') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijeras' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar():
    eleccion_computadora = obtener_eleccion_computadora()
    eleccion_usuario = obtener_eleccion_usuario()
    
    print(f"Computadora eligió: {eleccion_computadora}")
    print(f"Tú elegiste: {eleccion_usuario}")
    
    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(resultado)

if __name__ == "__main__":
    jugar()
