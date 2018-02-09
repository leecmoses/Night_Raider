import pygame
import time
import random

pygame.init()

# Screen Dimension
display_width = 1920
display_height = 1080

# Raider Dimension
raider_width = 224
raider_height = 154

# Asteroid Dimension
thingw = 64
thingh = 64

# Colors
# ref for picking colors: https://www.w3schools.com/colors/colors_picker.asp
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 204)
YELLOW = (255, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Night Raider')
clock = pygame.time.Clock()

# Music and Sound
pygame.mixer.music.load("music/Pontiac_Shuffle.mp3")
crash_sound = pygame.mixer.Sound("music/Boom.wav")


# Background
background_image = pygame.image.load("background/moon.png")

# Sprites
raiderImg = pygame.image.load('sprites/nightraider.png')
asteroidImg = pygame.image.load('sprites/asteroid.png')

# Classes

# Functions
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(round((count * 10) ** 1.3)), True, WHITE)
    gameDisplay.blit(text, (1820, 15))

def things(thingx, thingy):
    gameDisplay.blit(asteroidImg, (thingx, thingy))

def raider(x, y):
    gameDisplay.blit(raiderImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('GAME OVER!')

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Night Raider", largeText)
        TextRect.center = ((display_width / 2 + 100), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.draw.rect(gameDisplay, BLUE, ((display_width / 2) - 125 , 700, 200, 50))
        pygame.draw.rect(gameDisplay, YELLOW, ((display_width / 2) + 125 , 700, 200, 50))

        pygame.display.update()
        clock.tick(10)


# The Game loop ## ref intro for more on game.py
def game_loop():
    # Music
    pygame.mixer.music.play(-1)

    # Hide cursor
    pygame.mouse.set_visible(False)

    # Raider inital location
    x = (display_width * 0.1)
    y = (display_height * 0.5) - (raider_height * 0.5)

    x_change = 0
    y_change = 0

    # Thing inital location
    thing_startx = display_width + 300
    thing_starty = random.randrange(0, display_height)
    thing_speed = 20
    thing_width = 64
    thing_height = 64

    # Score
    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LEFT:
                #     x_change = -10
                # if event.key == pygame.K_RIGHT:
                #     x_change = 10
                if event.key == pygame.K_UP:
                    y_change = -40
                if event.key == pygame.K_DOWN:
                    y_change = 40

            if event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #     x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        y += y_change

        gameDisplay.fill(BLACK)
        gameDisplay.blit(background_image, [0, 0])

        # Thing movement
        things(thing_startx, thing_starty)
        thing_startx -= thing_speed

        # Raider movement
        raider(x, y)
        things_dodged(dodged)

        # Defined boundaries
        if (x > display_width - raider_width or x < 0) or (y > display_height - raider_height or y < 0):
            crash()
            gameExit = True
        
        # Defined things random starting point and dodge count
        if thing_startx < 0:
            thing_startx = display_width + 350
            thing_starty = random.randrange(0, display_height)
            dodged += 1
            thing_speed += 2

        # Collision
        if x + raider_width > thing_startx:
            if (y > thing_starty and y + raider_height < thing_starty) or (y + raider_height > thing_starty + thing_height and y < thing_starty + thing_height):
                crash()

        pygame.display.update()
        clock.tick(120)

# game_intro()
game_loop()
pygame.quit()
quit()