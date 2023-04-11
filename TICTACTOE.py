import sys, pygame
import numpy as np

# constants
##geometric constants
WIDTH = 600
HEIGHT = 600
B_ROW = 3
B_COL = 3
LINEWIDTH = 15
Circle_RAD = 60
Circle_WID = 20
SPACE = 50
##colors
WHITE = (255,255,255)
BLACK = (66, 66, 66)
LINECOLOR = (23,145,135)
BGCOLOR = (28,170,156)
##functional constants
player = 1
game_over = False

# initializing pygame
pygame.init()
Display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
Display.fill(BGCOLOR)

#board
BOARD = np.zeros((B_ROW,B_COL))
#print(BOARD)

'''
# vertical lines
pygame.draw.line(Display,LINECOLOR,(200,10),(200,590),LINEWIDTH)
pygame.draw.line(Display,LINECOLOR,(400,10),(400,590),LINEWIDTH)
# horizontal lines
pygame.draw.line(Display,LINECOLOR,(10,200),(590,200),LINEWIDTH)
pygame.draw.line(Display,LINECOLOR,(10,400),(590,400),LINEWIDTH)
'''
# Functions

## Geometric Functions
def draw_fig():
    for row in range(B_ROW):
        for col in range(B_COL):
            if BOARD[row][col] == 1:
                pygame.draw.circle(Display,WHITE,(int((col*200)+100),int((row*200)+100)),Circle_RAD,Circle_WID)
            elif BOARD[row][col] == 2:
                #pygame.draw.circle(Display,BLACK,(int((col*200)+100),int((row*200)+100)),Circle_RAD,Circle_WID)
                pygame.draw.line(Display,BLACK,(col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),25)
                pygame.draw.line(Display,BLACK,(col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),25)

def draw_lines():
    # vertical lines
    pygame.draw.line(Display,LINECOLOR,(200,10),(200,590),LINEWIDTH)
    pygame.draw.line(Display,LINECOLOR,(400,10),(400,590),LINEWIDTH)
    # horizontal lines
    pygame.draw.line(Display,LINECOLOR,(10,200),(590,200),LINEWIDTH)
    pygame.draw.line(Display,LINECOLOR,(10,400),(590,400),LINEWIDTH)
draw_lines()

### Winning lines
def draw_horizontal(row, player):
    codY = row*200+100

    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    
    pygame.draw.line(Display,color,(15,codY),(WIDTH-15,codY),20)

def draw_vertical(col,player):
    codX = col*200+100

    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    
    pygame.draw.line(Display,color,(codX,15),(codX,HEIGHT-15),20)

def draw_daigonalRL(player):

    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    
    pygame.draw.line(Display,color,(15,HEIGHT-15),(WIDTH-15,15),20)

def draw_daigonalLR(player):

    if player == 1:
        color = WHITE
    elif player == 2:
        color = BLACK
    
    pygame.draw.line(Display,color,(WIDTH-15,HEIGHT-15),(15,15),20)

## logical functions
def available(row,col):
    return BOARD[row][col] == 0

    '''
    if BOARD[row][col] == 0:
        return True
    else:
        return False
    '''

def marked(row, col, player):
    BOARD[row][col] = player
#marked(0,0,1)
#marked(0,0,2)
#print(BOARD)

def b_full():
    for row in range(B_ROW):
        for col in range(B_COL):
            if BOARD[row][col] == 0:
                return False
    return True

### Winning conditions
def check_won(player):
    #vertical
    for col in range(B_COL):
        if BOARD[0][col] == player and BOARD[1][col] == player and BOARD[2][col] == player :
            draw_vertical(col,player)
            return True
    #horizontal
    for row in range(B_ROW):
        if BOARD[row][0] == player and BOARD[row][1] == player and BOARD[row][2] == player :
            draw_horizontal(row,player)
            return True
    #daigonalLR
    if BOARD[0][0] == player and BOARD[1][1] == player and BOARD[2][2] == player:
        draw_daigonalLR(player)
        return True
    #daigonalRL
    if BOARD[2][0] == player and BOARD[1][1] == player and BOARD[0][2] == player:
        draw_daigonalRL(player)
        return True

## restart function
def restart():
    
    Display.fill(BGCOLOR)
    draw_lines()

    for row in range(B_ROW):
        for col in range(B_COL):
            BOARD[row][col] = 0
    
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            #MOUSEx = event.pos[0]
            #MOUSEy = event.pos[1]
            
            cl_row = int(event.pos[1]//200)
            cL_col = int(event.pos[0]//200)
            
            #marked(cl_row,cL_col,1)
            #print(BOARD)

            if available(cl_row,cL_col):
                if player == 1:
                    marked(cl_row,cL_col,player)
                    if check_won(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    marked(cl_row,cL_col,player)
                    if check_won(player):
                        game_over = True
                    player = 1
                
                draw_fig()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                restart()
                player = 1
                game_over = False

    pygame.display.update()