import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)
BLACK = (0,0,0)
PURPLE = (148,0,211)
SKY = (135, 206, 235)
GRASS = (50,205,50)


# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Lets go!')
 
# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs + keyboards and mouse movements/pressess
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
    # Processing
    # 10px edge left, 30px edge right, 50px wide 70px high
    SkyRect = pygame.Rect(0, 0, 1000, 1000)
    GrassRect = pygame.Rect(0, 300, 1000, 120)
    
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    # pygame.draw.rect(surface, colour, rectangleObject)
    pygame.draw.rect(WINDOW, SKY, SkyRect)
    pygame.draw.rect(WINDOW, GRASS, GrassRect)
  
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()