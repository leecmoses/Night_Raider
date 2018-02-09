import pygame
import time
import random

pygame.init()

# Screen Dimension
display_width = 2000
display_height = 1200

# Raider Dimension
raider_width = 224
raider_height = 154

# Colors
# ref for picking colors: https://www.w3schools.com/colors/colors_picker.asp
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 204)
YELLOW = (255, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

# Sprites
raiderImg = pygame.image.load('sprites/nightraider.png')

# Classes
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def raider(x, y):
    gameDisplay.blit(raiderImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    game_loop()

def crash():
    message_display('You crashed')

# The Game loop ## ref intro for more on game.py
def game_loop():
    # Hide cursor
    pygame.mouse.set_visible(False)

    # Raider inital location
    x = (display_width * 0.1)
    y = (display_height * 0.5) - (raider_height * 0.5)

    x_change = 0
    y_change = 0

    # Thing inital location
    thing_startx = display_width + 400
    thing_starty = random.randrange(0, display_height)
    thing_speed = 20
    thing_width = 75
    thing_height = 75

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
                if event.key == pygame.K_UP:
                    y_change = -15
                if event.key == pygame.K_DOWN:
                    y_change = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        y += y_change

        gameDisplay.fill(WHITE)

        # Thing movement
        things(thing_startx, thing_starty, thing_width, thing_height, BLACK)
        thing_startx -= thing_speed

        # Raider movement
        raider(x, y)

        # Defined boundaries
        if (x > display_width - raider_width or x < 0) or (y > display_height - raider_height or y < 0):
            crash()
            gameExit = True
        
        # Defined things random starting point
        if thing_startx < 0:
            thing_startx = display_width + 350
            thing_starty = random.randrange(0, display_height)


        if x + raider_width > thing_startx:
            if (y > thing_starty and y - raider_height < thing_starty) or (y - raider_height < thing_starty - thing_height and y > thing_starty - thing_height):
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

# Part 7 - Crashing
#  if y < thing_starty + thing_height:
#             print('y crossover')

#             if x > thing_startx and x < thing_startx + thing_width or x + raider_width > thing_startx and x + raider_width < thing_startx + thing_width:
#                 print ('x crossover')
#                 crash()