def preguntas_joel():
    preguntas = [
        "¿Quieres que vaya contigo a ver el Demonio Joel :3?",
        "¿Nos casamos?"
    ]

    for pregunta in preguntas:
        respuesta = input(pregunta + " (sí/no): ").lower()
        if respuesta == 'si' or respuesta == 'sí':
            respuesta_personalizada = input("¿Qué te gustaría hacer? ")
            if respuesta_personalizada:
                print("No tengo respuesta ahora para tu propuesta de: ", respuesta_personalizada)
            else:
                print("¡Genial! ¡Prepárate para la aventura!")
        else:
            print("¡Qué lástima! ¡Pensé que te gustaría!")
        print()

# Ejecutar la función
preguntas_joel()

print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ TE QUIERO JOEL ANALYTICS♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")