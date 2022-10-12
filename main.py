"""
Screen: 1200px x 600px
Character: 44px x 120px

"""
import sys
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

font_big = pygame.font.Font('Images/Pixel.ttf', 50)
font_small = pygame.font.Font('Images/Pixel.ttf', 25)

def write_text(text, color,font, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj, textrect)
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

# GAME LOOP -----------------------------------------------------------------------------------
def main_game():
    running = True
    main_player = Player(10,150)
    
    while running:

        clock.tick(56)
        select = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    main_player.playerX_Change = - 5
                    main_player.left = True
                    main_player.right = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    main_player.playerX_Change = 5
                    main_player.left = False
                    main_player.right = True
                if event.key == pygame.K_w:
                    select = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    main_player.playerX_Change = 0.0
                    main_player.left = False
                    main_player.right = False
                    main_player.walk_count = 0
        
        # Update the X-Axis Position of the Player
        main_player.playerX += main_player.playerX_Change
        
        # Boundaries
        if main_player.playerX <= 10:
            main_player.playerX = 10
        elif main_player.playerX >= 1050: # 675 because the player image is 125width (800 - 125 = 675)
            main_player.playerX = 1050

        if main_player.playerX >= 930 and select:
            selection_menu()

        main_player.walk_count
    
        screen.blit(bg,(0,0)) # change to background later screen.blit(bg, (0,0))
        main_player.drawPlayer(screen)
        screen.blit(counter,(650,310))
        pygame.display.update()


def selection_menu():
    choosing = True
    chosen_index = 0

    item0 = pygame.Rect(680,90,95,95)
    item1 = pygame.Rect(780,90,95,95)
    item2 = pygame.Rect(880,90,95,95)
    item3 = pygame.Rect(980,90,95,95)
    item4 = pygame.Rect(1080,90,95,95)

    item_list = {
        0:["Kapeng Barako",item0],
        1:["Soya Milk",item1],
        2:["Pandesal",item2],
        3:["Ensaymada",item3],
        4:["Suman",item4]
    }
    while choosing:
        
        rect = pygame.Rect(660,40,528,152)
        pygame.draw.rect(screen,(41, 41, 41), rect)

        pygame.draw.rect(screen,(118, 148, 163),item0)
        pygame.draw.rect(screen,(118, 148, 163),item1)
        pygame.draw.rect(screen,(118, 148, 163),item2)
        pygame.draw.rect(screen,(118, 148, 163),item3)
        pygame.draw.rect(screen,(118, 148, 163),item4)
        pygame.draw.rect(screen,(255, 137, 41),item_list[chosen_index][1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choosing = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    choosing = False
                if event.key == pygame.K_w:
                    return (chosen_index)
                if event.key == pygame.K_d:
                    chosen_index += 1
                    if chosen_index > 4:
                        chosen_index = 0
                if event.key == pygame.K_a:
                    chosen_index -= 1
                    if chosen_index < 0:
                        chosen_index = 4

        write_text(item_list[chosen_index][0],(255,255,255),font_small,847,55)
        pygame.display.update()

main_game()