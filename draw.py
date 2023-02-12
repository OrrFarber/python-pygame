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
    rectangle1 = pygame.Rect(100, 30, 50, 70)
    rectangle2 = pygame.Rect(200, 30, 100, 120)
    rectangle3 = pygame.Rect(230, 0, 200, 120)
    # pygame.draw.ellipse (surface, colour, rect, width) # width is optional
    ellipse1 = pygame.Rect(70, 200, 40, 100)
    # POLYGON points: 
    polygonPoints = ((70, 140), (100, 120), (110, 160), (100, 200), (90, 180))

    
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    # pygame.draw.rect(surface, colour, rectangleObject)
    pygame.draw.rect(WINDOW, RED, rectangle1)
    pygame.draw.rect(WINDOW, BLUE, rectangle2)
    pygame.draw.rect(WINDOW, GREEN, rectangle3, 2)
    #circle pygame.draw.circle(surface, colour, center, radius, width) # width is optional
    pygame.draw.circle(WINDOW, BLACK, (200, 50), 30)
    pygame.draw.circle(WINDOW, BLUE, (400, 200), 40, 2)
    # pygame.draw.circle(surface, colour, center, radius, width, topRight, topLeft, bottomLeft, bottomRight)
    pygame.draw.circle(WINDOW, RED, (200, 220), 50, 50, True, False, True, False)

    pygame.draw.ellipse(WINDOW, GREEN, ellipse1)
    # pygame.draw.line(surface, colour, (startX, startY), (endX, endY), width)
    pygame.draw.line(WINDOW, BLACK, (420, 30), (480, 200), 3)
    # pygame.draw.polygon(surface, colour, points, width) # width is optional
    pygame.draw.polygon(WINDOW, PURPLE, ((500, 140), (130, 120), (180, 160), (120, 200), (110, 180)))
    pygame.draw.polygon(WINDOW, GREEN, polygonPoints, 3)

    pygame.display.update()
    print (rectangle1.left)
    fpsClock.tick(FPS)
 
main()