#MODIFICACIONES REALIZADAS:
#Cambiar los colores de las imagenes
#Colocarle nombre a la pantalla del juego
#Cambiar los valores de gravedad y caida para que el pajarito caiga mas rapido y este mas lento
#Cambiar self.gap de tal manera que cada vez que el jugador pase por una tueria el ancho de estas disminuya
#Falta cambiar el puntaje, lo cual no se ha podido hacer.

import pygame
import sys
import random
pygame.init()

score=0
fuente=pygame.font.SysFont("Cambria", 30)
class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((577,500))
        self.caption = pygame.display.set_caption("Flappy Bird")
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("fondojuego.png")
        self.birdSprites = [pygame.image.load("0.png"),
                            pygame.image.load("1.png"),
                            pygame.image.load("2.png"),
                            pygame.image.load("dead.png")]
        self.wallUp = pygame.image.load("tuberiab.png")
        self.wallDown = pygame.image.load("tuberiat.png")
        self.gap = 200
        self.wallx = 250
        self.birdY = 200
        self.jump = 0
        self.jumpSpeed = 5
        self.gravity = 0.5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)
        self.puntaje=fuente.render("Score:"+str(score),1, (0,0,0))
        self.screen.blit(self.puntaje, (5, 10))

    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -90:
            self.wallx = 250
            self.counter += 1
            self.offset = random.randint(-50, 50)
            self.gap -= 10

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 0.5
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.birdY += self.gravity
            self.gravity += 0.1
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())

        if upRect.colliderect(self.bird):
            self.dead = True
        if downRect.colliderect(self.bird):
            self.dead = True
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-80, 80)
            self.gravity = 0.5

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Cambria", 30)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                pygame.display.flip()
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 15
                    self.gravity = 0.5
                    self.jumpSpeed = 10

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))

            if self.dead:
                self.sprite = 2
                self.gap = 200
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))

            if not self.dead:
                self.sprite = 0
            self.updateWalls()
            self.birdUpdate()
            pygame.display.update()

def gameover():
    over=True
    while over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    juego()
                if even.key==pygame.K_q:
                    pygame.quit()
        self.background=self.background.fill(blanco)
        letras=pygame.font.SysFont(None,30)
        texto=letras.render("Perdiste. C para continuar Q para salir del juego")


if __name__ == "__main__":
    FlappyBird().run()