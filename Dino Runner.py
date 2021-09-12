import pygame
import random

pygame.init()

#Window parameters
Height = 600
Width = 1100
screen = pygame.display.set_mode((Width,Height))
white = (255,255,255)

#load images
running = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
jumping = pygame.image.load("DinoJump.png")
ducking = [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
small_cactus = [pygame.image.load("SmallCactus1.png"),pygame.image.load("SmallCactus2.png"),pygame.image.load("SmallCactus3.png")]
large_cactus = [pygame.image.load("LargeCactus1.png"),pygame.image.load("LargeCactus2.png"),pygame.image.load("LargeCactus3.png")]
bird = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
cloudy = pygame.image.load("Cloud.png")
BG = pygame.image.load("Track.png")


class Dinosaur():
    x_pos = 80 
    y_pos = 310
    y_pos_duck = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = ducking
        self.run_img = running
        self.jump_img = jumping

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos


    def update(self,userinput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >=10:
            self.step_index = 0

        if userinput[pygame.K_UP] and not self.dino_jump:
            self.dino_run  = False
            self.dino_duck = False
            self.dino_jump = True

        elif userinput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        elif not (self.dino_jump or userinput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
            
    def run(self):
        self.image = self.run_img[self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index +=1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            
    def duck(self):
        self.image = self.duck_img[self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index +=1

    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))


class cloud:
    def __init__(self):
        self.x = Width + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.image = cloudy
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x <  -self.width :
            self.x = Width + random.randint(1800,2500)
            self.y = random.randint(50,100)
        

    def draw(self,screen):
         screen.blit(self.image,(self.x, self.y))

    
def main():
    run = True
    global game_speed
    game_speed=15
    clock = pygame.time.Clock()
    player = Dinosaur()
    Cloud = cloud()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(white)
        userinput = pygame.key.get_pressed()

        

        player.draw(screen)
        player.update(userinput)

        Cloud.draw(screen)
        Cloud.update()
        

        clock.tick(30)
        pygame.display.update()

main()
