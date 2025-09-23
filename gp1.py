import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Reglas: cada elemento vence a los que están en la lista
reglas = {
    "piedra": ["tijera"],
    "papel": ["piedra"],
    "tijera": ["papel"]
}

print("Juego: Piedra, Papel o Tijera")
print("Opciones:", opciones)

# Jugador elige
jugador = input("Elige una opción: ").lower()

# Validar entrada
if jugador not in opciones:
    print("Opción no válida. Intenta de nuevo.")
else:
    # Computadora elige
    pc = random.choice(opciones)
    print("Tú elegiste:", jugador)
    print("La computadora eligió:", pc)

    # Determinar ganador
    if jugador == pc:
        print("Resultado: Empate")
    elif pc in reglas[jugador]:
        print("Resultado: Tú ganas")
    else:
        print("Resultado: Gana la computadora")