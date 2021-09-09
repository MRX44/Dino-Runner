import pygame

pygame.init()

#Window parameters
Height = 600
Width = 1100
Screen = pygame.display.set_mode((Width,Height))

#load images
running = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
jumping = [pygame.image.load("DinoJump.png")]
ducking = [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
small_cactus = [pygame.image.load("SmallCactus1.png"),pygame.image.load("SmallCactus2.png"),pygame.image.load("SmallCactus3.png")]
large_cactus = [pygame.image.load("LargeCactus1.png"),pygame.image.load("LargeCactus2.png"),pygame.image.load("LargeCactus3.png")]
bird = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
cloud = pygame.image.load("Cloud.png")
BG = pygame.image.load("Track.png")


