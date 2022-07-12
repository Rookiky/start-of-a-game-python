import pygame
import pytmx
import pyscroll
pygame.init()


class Game:
    def __init__(self):
        screen = pygame.display.set_mode((800, 800))
        background = pygame.image.load("image_noire.jpg")
        screen.blit(background,(0,0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_u]:
            tmx_data = pytmx.util_pygame.load_pygame('innventaire.tmx')
            map_data = pyscroll.data.TiledMapData(tmx_data)
            map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
            map_layer.zoom = 2
            self.screen.update()




    def run(self):
        running = True

        while running:
            self..draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
