#imports
import sys, pygame
import numpy as np
from constants import *

# initializing pygame
pygame.init()
Display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
Display.fill(BGCOLOR)

class Board:
    def __init__(self):
        self.Sqrs = np.zeros((B_ROW,B_COL))
        print(self.Sqrs)

class Game:
    def __init__(self):
        self.BOARD = Board()
        self.draw_lines()

    def draw_lines(self):
        # vertical lines
        pygame.draw.line(Display,LINECOLOR,(200,10),(200,590),LINEWIDTH)
        pygame.draw.line(Display,LINECOLOR,(400,10),(400,590),LINEWIDTH)
        # horizontal lines
        pygame.draw.line(Display,LINECOLOR,(10,200),(590,200),LINEWIDTH)
        pygame.draw.line(Display,LINECOLOR,(10,400),(590,400),LINEWIDTH)

def main():
    game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()