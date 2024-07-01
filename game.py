import sys
import pygame

class Game():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.image = pygame.image.load("data/images/clouds/cloud_1.png")
        self.image.set_colorkey((0, 0, 0))

        self.img_pos = [160, 250]
        self.img_mov = [False, False, False, False]

        self.coll_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((16, 100, 155))            
            self.img_pos[1] += (self.img_mov[1] - self.img_mov[0]) * 5
            self.img_pos[0] += (self.img_mov[3] - self.img_mov[2]) * 5

            img_r = pygame.Rect(*self.img_pos, *self.image.get_size())

            if self.coll_area.colliderect(img_r):
                pygame.draw.rect(self.screen, (0, 50, 200), self.coll_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 150), self.coll_area)

            self.screen.blit(self.image, self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.img_mov[1] = True
                    elif event.key == pygame.K_UP:
                        self.img_mov[0] = True
                    elif event.key == pygame.K_LEFT:
                        self.img_mov[2] = True
                    elif event.key == pygame.K_RIGHT:
                        self.img_mov[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.img_mov[1] = False
                    elif event.key == pygame.K_UP:
                        self.img_mov[0] = False
                    elif event.key == pygame.K_LEFT:
                        self.img_mov[2] = False
                    elif event.key == pygame.K_RIGHT:
                        self.img_mov[3] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()