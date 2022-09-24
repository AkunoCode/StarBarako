"""
Screen: 1200px x 600px
Character: 44px x 120px

"""
import pygame

pygame.init()
# ELEMENTS ------------------------------------------------------------------------------------
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Devil's Diner")
# icon = pygame.image.load('Pinky_in_Space\Images\space-pig_Icon.png')
# pygame.display.set_icon(icon)
clock = pygame.time.Clock()

bg = pygame.image.load('Images\Background.png')
counter = pygame.image.load('Images\counter.png')

# PLAYER --------------------------------------------------------
playerIMG = pygame.image.load('Images\Player\Player_0.png')
walkL = [pygame.image.load('Images\Player\Player_L1.png'),pygame.image.load('Images\Player\Player_L2.png'),pygame.image.load('Images\Player\Player_L3.png'),pygame.image.load('Images\Player\Player_L4.png')]
walkR = [pygame.image.load('Images\Player\Player_R1.png'),pygame.image.load('Images\Player\Player_R2.png'),pygame.image.load('Images\Player\Player_R3.png'),pygame.image.load('Images\Player\Player_R4.png')]

class Player(object):
    def __init__(self, x, y):
        self.playerX = x
        self.playerY = y
        self.playerX_Change = 0
        self.left = False
        self.right = False
        self.walk_count = 0
    
    def drawPlayer(self,screen):
        if self.walk_count + 1 >=28:
            self.walk_count = 0
        if self.left:
            screen.blit(walkL[self.walk_count//7], (self.playerX,self.playerY))
            self.walk_count += 1
        elif self.right:
            screen.blit(walkR[self.walk_count//7], (self.playerX,self.playerY))
            self.walk_count += 1
        else:
            screen.blit(playerIMG, (self.playerX,self.playerY))

def player(x,y):
    screen.blit(playerIMG,(x,y))

def updateWindow():
    main_player.walk_count
    
    screen.blit(bg,(0,0)) # change to background later screen.blit(bg, (0,0))
    main_player.drawPlayer(screen)
    screen.blit(counter,(650,310))
    pygame.display.update()


# GAME LOOP -----------------------------------------------------------------------------------
running = True
main_player = Player(0,150)

while running:

    clock.tick(56)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main_player.playerX_Change = - 4
                main_player.left = True
                main_player.right = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_player.playerX_Change = 4
                main_player.left = False
                main_player.right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_player.playerX_Change = 0.0
                main_player.left = False
                main_player.right = False
                main_player.walk_count = 0
    
    # Update the X-Axis Position of the Player
    main_player.playerX += main_player.playerX_Change
    
    # Boundaries
    if main_player.playerX <= 0:
        main_player.playerX = 0
    elif main_player.playerX >= 1135: # 675 because the player image is 125width (800 - 125 = 675)
       main_player.playerX = 1135

    updateWindow()