import pygame
import sys

pygame.init()

# Configuración de pantalla y colores
ANCHO, ALTO = 1000, 800
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
AZUL = (0, 0, 255)
GRIS = (200, 200, 200)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Agregar Preguntas")

# Fuentes y texto inicial
fuente = pygame.font.Font(None, 36)
input_text = ""  # Texto que el usuario está escribiendo
mensaje = ""  # Mensaje de feedback
dificultad = "Fácil"  # Dificultad inicial

# Botones para las dificultades
botones_dificultad = {
    "Fácil": pygame.Rect(150, 500, 200, 60),
    "Media": pygame.Rect(400, 500, 200, 60),
    "Difícil": pygame.Rect(650, 500, 200, 60),
}

# Botón para guardar
boton_guardar = pygame.Rect(400, 600, 200, 60)

# Bucle principal
ejecutando = True
while ejecutando:
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        # Manejar entrada de texto
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif evento.key == pygame.K_RETURN:  # Presiona Enter para guardar
                mensaje = f"Pregunta guardada con dificultad: {dificultad}"
                input_text = ""
            else:
                input_text += evento.unicode

        # Manejar clics del ratón
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for nivel, rect in botones_dificultad.items():
                if rect.collidepoint(pos):
                    dificultad = nivel
            if boton_guardar.collidepoint(pos):
                mensaje = f"Pregunta guardada con dificultad: {dificultad}"
                input_text = ""

    # Dibujar cuadro de entrada
    pygame.draw.rect(pantalla, BLANCO, (150, 200, 700, 60), border_radius=5)
    texto_input = fuente.render(input_text, True, NEGRO)
    pantalla.blit(texto_input, (160, 210))

    # Dibujar botones de dificultad
    for nivel, rect in botones_dificultad.items():
        color = VERDE if nivel == dificultad else GRIS
        pygame.draw.rect(pantalla, color, rect, border_radius=5)
        texto_nivel = fuente.render(nivel, True, NEGRO if nivel == dificultad else BLANCO)
        pantalla.blit(texto_nivel, (rect.x + 50, rect.y + 15))

    # Dibujar botón de guardar
    pygame.draw.rect(pantalla, AZUL, boton_guardar, border_radius=5)
    texto_guardar = fuente.render("Guardar Pregunta", True, BLANCO)
    pantalla.blit(texto_guardar, (boton_guardar.x + 20, boton_guardar.y + 15))

    # Mostrar mensaje de feedback
    texto_mensaje = fuente.render(mensaje, True, VERDE)
    pantalla.blit(texto_mensaje, (150, 700))

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()
