import pygame
import snake_logica as snk

tam = 10
tick = 10

def main():
    pygame.init()
    pygame.mixer.init()
    snk.init()
    ancho = snk.columnas * tam
    alto = snk.filas * tam
    window = pygame.display.set_mode((ancho, alto))
    font = pygame.font.SysFont('Arial', 18)
    clock = pygame.time.Clock()

    # Cargar sonidos
    sonido_comer = pygame.mixer.Sound("8-bit-coin-pickup.wav")
    sonido_morir = pygame.mixer.Sound("retro_game_death_sound.wav")
    pygame.mixer.music.load("Lenny Pixels - Stay Connected - 8bit.mp3")
    pygame.mixer.music.play(-1)

    loop = True
    contador_parpadeo = 0
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    snk.cambiar_direccion(snk.Direccion.ARRIBA)
                elif keys[pygame.K_DOWN]:
                    snk.cambiar_direccion(snk.Direccion.ABAJO)
                elif keys[pygame.K_RIGHT]:
                    snk.cambiar_direccion(snk.Direccion.DERECHA)
                elif keys[pygame.K_LEFT]:
                    snk.cambiar_direccion(snk.Direccion.IZQUIERDA)
                elif keys[pygame.K_r]:
                    main()
                elif keys[pygame.K_ESCAPE]:
                    loop = False

        # Dibujar
        
        
        if not snk.serpiente["viva"]:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
                sonido_morir.play()
            if contador_parpadeo > 5:
                window.fill((255, 0, 0))
                contador_parpadeo = 0
            else:
                window.fill((0, 0, 0))
            contador_parpadeo += 1
        else:
            window.fill((0, 0, 0))

        # Dibuja las líneas de la cuadrícula
        for c in range(snk.columnas):
            pygame.draw.line(window, (40, 40, 40), (c * tam, 0), (c * tam, alto))
        for f in range(snk.filas):
            pygame.draw.line(window, (40, 40, 40), (0, f * tam), (ancho, f * tam))

        for f in range(snk.filas):
            for c in range(snk.columnas):
                x = c * tam
                y = f * tam
                if snk.matriz[f][c] == snk.MANZANA:
                    pygame.draw.rect(window, (255, 0, 0), (x, y, tam, tam))
                elif snk.matriz[f][c] == snk.DORADA:
                    pygame.draw.rect(window, (255, 215, 0), (x, y, tam, tam))
                elif snk.matriz[f][c] == snk.VENENO:
                    pygame.draw.rect(window, (128, 0, 128), (x, y, tam, tam))
                elif snk.matriz[f][c] > snk.VACIA:
                    pygame.draw.rect(window, (255, 255, 255), (x, y, tam, tam))
        
        # Mostrar manzanas comidas.
        puntuacion = snk.serpiente["manzanas_comidas"]
        puntuacion_anterior = puntuacion
        texto = font.render(f"Manzanas comidas: {puntuacion}", True, (255, 255, 255))
        window.blit(texto, (5, 5))

        snk.avanzar()
        if snk.serpiente["manzanas_comidas"] > puntuacion_anterior:
            sonido_comer.play()

        pygame.display.update()

        # Aumentar velocidad al comer más manzanas.
        clock.tick(tick + puntuacion)

    pygame.quit()

#main()

if __name__ == '__main__':
    main()