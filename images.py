import pygame

#  BACKGROUND PROPERTIES -------------------------------------------------------------------------------
bg = pygame.image.load('Images\Background.png')
counter = pygame.image.load('Images\counter.png')

# MENU PROPERTIES ---------------------------------------------------------------------------------------
chalkboard = pygame.image.load('Images\Chalkboard.png')
selector_m = pygame.image.load('Images\Food-Menu\Selector-m.png')
ensaymada_m = pygame.image.load('Images\Food-Menu\Menu-Ensaymada.png')
pandesal_m = pygame.image.load('Images\Food-Menu\Menu-Pandesal.png')
spanish_m = pygame.image.load('Images\Food-Menu\Menu-Spanish.png')
kape_m = pygame.image.load('Images\Food-Menu\Menu-Coffee.png')
gatas_m = pygame.image.load('Images\Food-Menu\Menu-Milk.png')

# PLAYER ----------------------------------------------------------------------------------------------------
player = pygame.image.load('Images\Player\Player_0.png')
PlayerIMG_R = pygame.transform.scale(player,(180,320))
PlayerIMG_L = PlayerR = pygame.transform.flip(PlayerIMG_R, True, False)

Player_Sprite = [
    pygame.image.load('Images\Player\Player_R1.png'),
    pygame.image.load('Images\Player\Player_R2.png'),
    pygame.image.load('Images\Player\Player_R3.png'),
    pygame.image.load('Images\Player\Player_R4.png'),
    pygame.image.load('Images\Player\Player_R5.png'),
    pygame.image.load('Images\Player\Player_R6.png'),
    pygame.image.load('Images\Player\Player_R7.png'),
    pygame.image.load('Images\Player\Player_R8.png'),]

walkR = []
for image in Player_Sprite:
    Player = pygame.transform.scale(image,(180,320))
    walkR.append(Player)

walkL = []

for image in walkR:
    PlayerL = pygame.transform.flip(image, True, False)
    walkL.append(PlayerL)