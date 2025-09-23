import random

def iniciar_juego():
    print("⚡ Bienvenido a 'Adivina la Energía' ⚡")
    print("Debes decir si la fuente de energía es renovable o no renovable.")
    print("Escribe 'r' para renovable o 'n' para no renovable.\n")

    fuentes = {
        "Solar": "r",
        "Eólica": "r",
        "Hidráulica": "r",
        "Biomasa": "r",
        "Geotérmica": "r",
        "Carbón": "n",
        "Petróleo": "n",
        "Gas natural": "n",
        "Nuclear": "n"
    }

    puntos = 0
    rondas = 5
    opciones = list(fuentes.keys())

    for i in range(rondas):
        fuente = random.choice(opciones)
        respuesta = input(f"🔋 ¿La fuente '{fuente}' es renovable (r) o no renovable (n)? ").lower()

        if respuesta == fuentes[fuente]:
            print("bien ¡Correcto!\n")
            puntos += 1
        else:
            tipo = "renovable" if fuentes[fuente] == "r" else "no renovable"
            print(f"mal Incorrecto. '{fuente}' es una fuente {tipo}.\n")

    print(f"🎉 Juego terminado. Obtuviste {puntos} de {rondas} puntos.")

if __name__ == "__main__":
    iniciar_juego()
