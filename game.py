import pygame
import pytmx
import pyscroll

from player import Player
from pnj import Pnj
from attack import Enemy


pygame.init()

class Game:
    def __init__(self):
        self.player = None
        self.pnj = None
        self.screen = pygame.display.set_mode((800, 800))
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        #générer un joueur:
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        pnj_position = tmx_data.get_object_by_name("pnj")
        self.pnj = Pnj(pnj_position.x, pnj_position.y)



        #générer les obstacles de collision
        self.mur = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.mur.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        #générer les layers de la map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
        self.group.add(self.pnj)

        #définir rect pour entrer maison
        #entrer_maison = tmx_data.get_object_by_name('entrer_maison')
        #self.entrer_maison_rect = pygame.Rect(entrer_maison.x, entrer_maison.y, entrer_maison.width, entrer_maison.height)




    def gerer_commande(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_z]:
            self.player.haut()
            self.player.changer_animation('haut')
        elif pressed[pygame.K_q]:
            self.player.gauche()
            self.player.changer_animation('gauche')
        elif pressed[pygame.K_d]:
            self.player.droite()
            self.player.changer_animation('droite')
        elif pressed[pygame.K_s]:
            self.player.bas()
            self.player.changer_animation('bas')

    def gerer_commande1(self):
        pressed1 = pygame.key.get_pressed()
        if pressed1[pygame.K_UP]:
            self.pnj.haut()
            self.pnj.changer_animation('haut')
            #images = ['adventurer-run3-00.png', 'adventurer-run3-01.png', 'adventurer-run3-02.png']
            #index = 0
            #while True:
                #index += 1
                # Modulo to keep the index in the correct range.
                #index %= len(images)
                #current_image = images[index]
                #self.screen.blit(current_image, images.index)
            print("haut")
        elif pressed1[pygame.K_DOWN]:
            self.pnj.bas()
            self.pnj.changer_animation('bas')
        elif pressed1[pygame.K_LEFT]:
            self.pnj.gauche()
            self.pnj.changer_animation('gauche')
        elif pressed1[pygame.K_RIGHT]:
            self.pnj.droite()
            self.pnj.changer_animation('droite')





    #def changer_maison(self):
        #tmx_data = pytmx.util_pygame.load_pygame('maisoninte1.tmx')
        #map_data = pyscroll.data.TiledMapData(tmx_data)
        #map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #map_layer.zoom = 1.5

        # générer les obstacles de collision
        #self.mur = []

        #for obj in tmx_data.objects:
            #if obj.type == "collision":
                #self.mur.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les layers de la map
        #self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        #self.group.add(self.player)

        # définir rect pour entrer maison
        #entrer_maison = tmx_data.get_object_by_name('sortie_maison')
        #self.entrer_maison_rect = pygame.Rect(entrer_maison.x, entrer_maison.y, entrer_maison.width, entrer_maison.height)

        #spawn_point_maison = tmx_data.get_object_by_name("entrer_maison_entrer")
        #self.player_position[0] = spawn_point_maison.x
        #self.player_position[1] = spawn_point_maison.y - 20




    #def changer_monde(self):
        #tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        #map_data = pyscroll.data.TiledMapData(tmx_data)
        #map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #map_layer.zoom = 1.5

        # générer les obstacles de collision
        #self.mur = []

        #for obj in tmx_data.objects:
            #if obj.type == "collision":
                #self.mur.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # générer les layers de la map
        #self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        #self.group.add(self.player)

        # définir rect pour entrer maison
        #entrer_maison = tmx_data.get_object_by_name('entrer_maison')
        #self.entrer_maison_rect = pygame.Rect(entrer_maison.x, entrer_maison.y, entrer_maison.width, entrer_maison.height)

        #definir point de spawn
        #spawn_point_maison = tmx_data.get_object_by_name("entrer_maison_sortie")
        #self.player_position[0] = spawn_point_maison.x
        #self.player_position[1] = spawn_point_maison.y + 20




    def update(self):
        self.group.update()

        #if self.map =='map.tmx' and self.player.pieds.collidelist(self.entrer_maison_rect):
            #self.changer_monde()
            #self.map = pytmx.util_pygame.load_pygame('maisoninte1.tmx')

        #verifier entrer maison
        #if self.map =='maisoninte1.tmx' and self.player.pieds.collidelist(self.entrer_maison_rect):
            #self.changer_monde()
            #self.map = 'map.tmx'

        for sprite in self.group.sprites():
            if sprite.pieds.collidelist(self.mur) > -1:
                sprite.revenir_position()



    #maintient la fenêtre du jeu ouverte
    def run(self):
        running = True

        while running:
            self.player.enregistrer_location()
            self.pnj.enregistrer_location()
            self.gerer_commande()
            self.gerer_commande1()
            self.group.center(self.player.rect)
            self.update()
            self.group.draw(self.screen)
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
