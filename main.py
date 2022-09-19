"""
Screen: 1200px x 600px
Character: 44px x 100px

"""
import pygame

pygame.init()
# ELEMENTS ------------------------------------------------------------------------------------
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Devil's Diner")
# icon = pygame.image.load('Pinky_in_Space\Images\space-pig_Icon.png')
# pygame.display.set_icon(icon)

# PLAYER --------------------------------------------------------
playerIMG = pygame.image.load('Images\Player\Waiter_0.png')
playerIMG = pygame.transform.scale(playerIMG, (64,120))
playerX = 20
playerY = 340
playerX_change = 0

def player(x,y):
    screen.blit(playerIMG,(x,y))




# GAME LOOP -----------------------------------------------------------------------------------
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = - 0.3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.0
    
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1156: # 675 because the player image is 125width (800 - 125 = 675)
        playerX = 1156

    player(playerX, playerY)
    pygame.display.update()