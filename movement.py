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
CHARACTER = (255, 30, 70)

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
 
  characterX = 10
  characterY = 30
  characterWidth = 50
  characterHeight = 70
  
  
  character2X = 530
  character2Y = 30
  character2Width = 50
  character2Height = 70
  
  # The main game loop
  while looping :
    # Get inputs + keyboards and mouse movements/pressess
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
        
      if event.type == pygame.KEYDOWN and event.key == K_r :
        characterX = 10
        characterY = 30
 
# keys = pygame.key.get_pressed()
    pressed = pygame.key.get_pressed()
    if (pressed[K_d] ) :
      characterX = characterX + 3
    elif (pressed[K_a] ) :
        characterX = characterX -3
    elif(pressed[K_w] ) : 
        characterY = characterY - 3
    elif (pressed[K_s] ) :
        characterY = characterY + 3 
        
    # elif (pressed[K_RIGHT]) :
    #   character2X = character2X + 3
    # elif (pressed[K_LEFT]) :
    #     character2X = character2X -3
    # elif( pressed[K_UP]) : 
    #     character2Y = character2Y - 3
    # elif (pressed[K_DOWN]) :
    #     character2Y = character2Y + 3 
    
    # Processing
    # 10px edge left, 30px edge right, 50px wide 70px high
    SkyRect = pygame.Rect(0, 0, 1000, 1000)
    GrassRect = pygame.Rect(0, 300, 1000, 120)
    character = pygame.Rect(characterX, characterY, characterWidth, characterHeight)
    character2 = pygame.Rect(character2X, character2Y, character2Width, character2Height)
    
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    # pygame.draw.rect(surface, colour, rectangleObject)
    pygame.draw.rect(WINDOW, SKY, SkyRect)
    pygame.draw.rect(WINDOW, GRASS, GrassRect)
    pygame.draw.rect(WINDOW, CHARACTER, character)
    # pygame.draw.rect(WINDOW, PURPLE, character2)

  
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()