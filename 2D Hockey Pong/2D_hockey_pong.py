import pygame, sys, random


def puck_animation():
    global puck_speed_x, puck_speed_y

    # Animation
    puck.x += puck_speed_x
    puck.y += puck_speed_y

    #  Collision
    if puck.top <= 0 or puck.bottom >= WINDOW_HEIGHT:
        puck_speed_y *= -1
        pygame.mixer.music.load('Hockey_Puck_Sound.mp3')
        pygame.mixer.music.play(0)
    if puck.left <= 0 or puck.right >= WINDOW_WIDTH:
        puck_restart()

    if puck.colliderect(player_one) or puck.colliderect(player_two):
        puck_speed_x *= -1
        pygame.mixer.music.load('Hockey_Stick_Sound_Effect_HD.mp3')
        pygame.mixer.music.play(0)

def player_one_animation():
    #Animation
    player_one.y += player_one_speed

    #Player One Collision
    if player_one.top <= 0:
        player_one.top = 0
    if player_one.bottom >= WINDOW_HEIGHT:
        player_one.bottom = WINDOW_HEIGHT

def player_two_animation():
    #Animation
    if player_two.top < puck.y:
        player_two.top += player_two_speed
    if player_two.bottom > puck.y:
        player_two.bottom -= player_two_speed

    #Player Two Collision
    if player_two.top <= 0:
        player_two.top = 0
    if player_two.bottom >= WINDOW_HEIGHT:
        player_two.bottom = WINDOW_HEIGHT

def puck_restart():
    global puck_speed_x, puck_speed_y
    puck.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    puck_speed_x *= random.choice((1,-1))
    puck_speed_y *= random.choice((1,-1))


#Setup
pygame.init()
clock = pygame.time.Clock()


#Creating Window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("2D Hockey Pong")

logo = pygame.image.load("rangers.png")

# Game Objects
puck = pygame.Rect(WINDOW_WIDTH/2 - 15, WINDOW_HEIGHT/2 -15 , 30, 30)
player_one = pygame.Rect(WINDOW_WIDTH - 20, WINDOW_HEIGHT/2 - 70, 10, 140)
#player_one = pygame.image.load("player_one.png")
player_two = pygame.Rect(10 , WINDOW_HEIGHT/2 - 70, 10, 140)
#player_two = pygame.image.load("player_two.png")



# Colors
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
LIGHT_GREY = (200,200,200)

# Speeds
puck_speed_x = 7 * random.choice((1,-1))
puck_speed_y = 7 * random.choice((1,-1))
player_one_speed = 0
player_two_speed = 7

while True:
    #Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_one_speed += 7
            if event.key == pygame.K_UP:
                player_one_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_one_speed -= 7
            if event.key == pygame.K_UP:
                player_one_speed += 7

        if player_two.top < puck.y:
            player_two.top += player_two_speed
        if player_two.bottom > puck.y:
            player_two.bottom -= player_two_speed
        if player_two.top <= 0:
            player_two.top = 0
        if player_two.bottom >= WINDOW_HEIGHT:
            player_two.bottom = WINDOW_HEIGHT




    puck_animation()
    player_one_animation()
    player_two_animation()





    # Visuals
    window.fill(WHITE)
    pygame.draw.aaline(window, LIGHT_GREY, (WINDOW_WIDTH/2,0), (WINDOW_WIDTH/2, WINDOW_HEIGHT))
    pygame.draw.rect(window, RED, player_one)
    #window.blit(player_one,(WINDOW_WIDTH - 105, WINDOW_HEIGHT/2 - 80))
    pygame.draw.rect(window, BLUE, player_two)
    #window.blit(player_two,(10 , WINDOW_HEIGHT/2 - 70))
    window.blit(logo, (WINDOW_WIDTH/2.93,WINDOW_HEIGHT/3.5))
    pygame.draw.ellipse(window, BLACK, puck)







    # Updating the window
    pygame.display.flip()
    clock.tick(60)
