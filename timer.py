import pygame
from agregar_pregunta import *

import pygame

pygame.init()

# Configuración inicial
timer = pygame.time.Clock()
tiempo_restante = 30
fuente = pygame.font.Font(None, 74)
vidas = 3

while vidas > 0:
    # Calcular el tiempo transcurrido
    tiempo_transcurrido = timer.tick(60) / 1000
    tiempo_restante -= tiempo_transcurrido

    # Verificar si el tiempo se acabó
    if tiempo_restante <= 0:
        vidas -= 1
        tiempo_restante = 30

    # Renderizar el temporizador
    texto_timer = fuente.render(f"Tiempo restante: {int(tiempo_restante)} | Vidas: {vidas}", True, (255, 255, 255))

    # Esto es solo para mostrar que todo funciona
    print(f"Tiempo restante: {int(tiempo_restante)} | Vidas: {vidas}")
