"""
Screen: 1200px x 600px
Character: 44px x 120px

"""
import sys
import pygame
from images import *

pygame.init()
# ELEMENTS ------------------------------------------------------------------------------------
screen = pygame.display.set_mode((1200, 675))
pygame.display.set_caption("Starbarako")
# icon = pygame.image.load('Pinky_in_Space\Images\space-pig_Icon.png')
# pygame.display.set_icon(icon)
clock = pygame.time.Clock()

font_big = pygame.font.Font('Images/Pixel.ttf', 50)
font_small = pygame.font.Font('Images/Pixel.ttf', 25)

order_item = [kape,gatas,ensaymada,spanish,pandesal]

def write_text(text, color,font, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    screen.blit(textobj, textrect)
# PLAYER --------------------------------------------------------

class Player(object):
    def __init__(self, x, y):
        self.playerX = x
        self.playerY = y
        self.playerX_Change = 0
        self.left = False
        self.right = False
        self.walking = False
        self.walk_count = 0
    
    def drawPlayer(self,screen):
        if self.walk_count >= 32:
            self.walk_count = 0
        if self.left and self.walking:
            screen.blit(walkL[self.walk_count//8], (self.playerX,self.playerY))
            self.walk_count += 1
        elif self.right and self.walking:
            screen.blit(walkR[self.walk_count//8], (self.playerX,self.playerY))
            self.walk_count += 1
        elif self.left:
            screen.blit(PlayerIMG_L, (self.playerX,self.playerY))
        elif self.right:
            screen.blit(PlayerIMG_R, (self.playerX,self.playerY))

            

# GAME LOOP -----------------------------------------------------------------------------------
def main_game():
    running = True
    main_player = Player(10,245)
    main_player.right = True
    order = False
    leave = False
    while running:

        clock.tick(56)
        select = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    main_player.playerX_Change = - 4.5
                    main_player.right = False
                    main_player.left = True
                    main_player.walking = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    main_player.playerX_Change = 4.5
                    main_player.left = False
                    main_player.right = True
                    main_player.walking = True
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    select = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    select = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    main_player.playerX_Change = 0.0
                    main_player.walking = False
                    main_player.walk_count = 0
        
        
        # Update the X-Axis Position of the Player
        main_player.playerX += main_player.playerX_Change
        
        # Boundaries
        if main_player.playerX <= 10:
            main_player.playerX = 10
        elif main_player.playerX >= 1010: # 675 because the player image is 125width (800 - 125 = 675)
            main_player.playerX = 1010
        if main_player.playerX >= 930 and select:
            order_number = selection_menu()
            order = True

        # LEAVING ITEM ON THE TABLE
        if (main_player.playerX >= 10 and main_player.playerX <= 540) and select and order:
            leave = True
            order = False
            left_order = order_item[order_number]

    
        # DRAW SECTION --------------------------------------------------------------------------------------------
        screen.blit(bg,(0,0))
        screen.blit(chalkboard,(656,90))
        screen.blit(kape_m,(680,150))
        screen.blit(gatas_m,(780,150))
        screen.blit(ensaymada_m,(880,150))
        screen.blit(spanish_m,(980,150))
        screen.blit(pandesal_m,(1080,150))
        
        screen.blit(chair,(60,390))
        screen.blit(table,(210,420))
        screen.blit(chair2,(400,390))

        # LEAVING ITEM ON TABLE
        if leave:
            screen.blit(left_order,(275,380))

        main_player.drawPlayer(screen)
        
        # PICKING UP ITEM ON THE MENU
        if order:
            if main_player.left:
                item_x = main_player.playerX
                item_y = main_player.playerY + (44*4)
            if main_player.right:
                item_x = main_player.playerX + (120)
                item_y = main_player.playerY + (44*4)
            screen.blit(order_item[order_number],(item_x,item_y))

        screen.blit(counter,(650,375))
        write_text("Today's Menu",(255,255,255),font_small,847,100)
        pygame.display.update()


def selection_menu():
    choosing = True
    chosen_index = 0

    item_list = {
        0:["Kapeng Barako",(680,150)],
        1:["Fresh Milk",(780,150)],
        2:["Ensaymada",(880,150)],
        3:["Spanish Bread",(980,150)],
        4:["Pandesal",(1080,150)]
    }

    while choosing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choosing = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    choosing = False
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    return chosen_index
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    chosen_index += 1
                    if chosen_index > 4:
                        chosen_index = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    chosen_index -= 1
                    if chosen_index < 0:
                        chosen_index = 4

        # DRAW SECTION -----------------------------------------------------------------------------------------
        screen.blit(chalkboard,(656,90))
        screen.blit(kape_m,(680,150))
        screen.blit(gatas_m,(780,150))
        screen.blit(ensaymada_m,(880,150))
        screen.blit(spanish_m,(980,150))
        screen.blit(pandesal_m,(1080,150))
        screen.blit(selector_m,item_list[chosen_index][1])
        write_text(item_list[chosen_index][0],(255,255,255),font_small,847,100)
        pygame.display.update()

main_game()