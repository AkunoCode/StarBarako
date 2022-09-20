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
clock = pygame.time.Clock()

# PLAYER --------------------------------------------------------
playerIMG = pygame.image.load('Images\Player\Player_0.png')
walkL = [pygame.image.load('Images\Player\Player_L1.png'),pygame.image.load('Images\Player\Player_L2.png'),pygame.image.load('Images\Player\Player_L3.png'),pygame.image.load('Images\Player\Player_L4.png')]
walkR = [pygame.image.load('Images\Player\Player_R1.png'),pygame.image.load('Images\Player\Player_R2.png'),pygame.image.load('Images\Player\Player_R3.png'),pygame.image.load('Images\Player\Player_R4.png')]

playerX = 20
playerY = 340
playerX_change = 0
left = False
right = False
walk_count = 0

def player(x,y):
    screen.blit(playerIMG,(x,y))

def updateWindow():
    global walk_count
    
    screen.fill((0,0,0)) # change to background later screen.blit(bg, (0,0))
    if walk_count + 1 >=28:
        walk_count = 0
    if left:
        screen.blit(walkL[walk_count//7], (playerX,playerY))
        walk_count += 1
    elif right:
        screen.blit(walkR[walk_count//7], (playerX,playerY))
        walk_count += 1
    else:
        screen.blit(playerIMG, (playerX,playerY))
    
    pygame.display.update()


# GAME LOOP -----------------------------------------------------------------------------------
running = True
while running:

    clock.tick(56)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = - 3
                left = True
                right = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 3
                left = False
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.0
                left = False
                right = False
                walk_count = 0
    
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 1135: # 675 because the player image is 125width (800 - 125 = 675)
        playerX = 1135

    updateWindow()