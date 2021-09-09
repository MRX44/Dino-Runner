import pygame

pygame.init()

#Window parameters
Height = 600
Width = 1100
screen = pygame.display.set_mode((Width,Height))
white = (255,255,255)

#load images
running = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
jumping = [pygame.image.load("DinoJump.png")]
ducking = [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
small_cactus = [pygame.image.load("SmallCactus1.png"),pygame.image.load("SmallCactus2.png"),pygame.image.load("SmallCactus3.png")]
large_cactus = [pygame.image.load("LargeCactus1.png"),pygame.image.load("LargeCactus2.png"),pygame.image.load("LargeCactus3.png")]
bird = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
cloud = pygame.image.load("Cloud.png")
BG = pygame.image.load("Track.png")


class Dinosaur():
    x_pos = 80 
    y_pos = 310

    def __init__(self):
        self.duck_img = ducking
        self.run_img = running
        self.jump_img = jumping

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

        


def main():
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(white)
        userinput = pygame.key.get_pressed()

        


        clock.tick(30)
        pygame.display.update()

main()
