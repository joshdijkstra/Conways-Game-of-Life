import sys, pygame
import numpy as np
import random

def coord_func(par):
    x = par[0]
    y = par[1]
    return [(sy/2)+y*sy,(sx/2)+x*sx]

pygame.init()
#image_size = 60
grid_size = 150
black = 0, 0, 0
green = (0, 255, 0)
board = np.zeros(shape=(grid_size,grid_size))
next_board = np.zeros(shape=(grid_size,grid_size))
for x in range(len(board)):
    for y in range(len(board)):
        board[x][y] = random.randint(0,1)
"""
board[4][5] = 1
board[5][5] = 1
board[6][5] = 1
board[6][4] = 1
board[5][3] = 1
"""

size = width, height = 60 * 15 , 60 * 15
sx = width/grid_size
sy = height/grid_size
screen = pygame.display.set_mode(size)
image = pygame.image.load("spore.png")
image = pygame.transform.scale(image, (sx,sy))
print(board)
print("##################################")
while 1:
    print(board)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    rects = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 1:
                coords = coord_func([x, y])
                rects.append(pygame.Rect(image.get_rect(center=(coords[0], coords[1]))))
    for x in range(len(rects)):
        screen.blit(image, rects[x])
    for x in range(len(board)):
        for y in range(len(board[x])):
            alive = 0
            try:
                alive += board[x-1][y-1]
            except:
                pass
            try:
                alive +=board[x-1][y]
            except:
                pass
            try:
                alive += board[x-1][y+1]
            except:
                pass
            try:
                alive += board[x+1][y-1]
            except:
                pass
            try:
                alive += board[x+1][y]
            except:
                pass
            try:
                alive +=   board[x+1][y+1]
            except:
                pass
            try:
                alive += board[x][y-1]
            except:
                pass
            try:
                alive += board[x][y+1]
            except:
                pass
            if board[x][y] == 1:
                if alive == 2 or alive ==3:
                    next_board[x][y] = 1
                elif alive < 2:
                    next_board[x][y] = 0
                else:
                    next_board[x][y] = 0
            if board[x][y] == 0:
                if alive == 3:
                    next_board[x][y] = 1
    board = next_board

    pygame.time.wait(50)
    pygame.display.flip()