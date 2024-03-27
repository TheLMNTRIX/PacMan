import pygame
import random


#Dimensions for window
board_width=28
board_height=31
cell_size = 24
window_width = board_width * cell_size 
window_height = board_height * cell_size + 40

BLACK=(0,0,0)
YELLOW=(255,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)


def create_board():
    board=[]
    #layout for the board, # is wall, blank is empty cell, * is Powerup, . is regular point
    layout = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#*####.#####.##.#####.####*#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "     #.##### ## #####.#     ",
    "     #.##          ##.#     ",
    "     #.## ###--### ##.#     ",
    "     #.## #      # ##.#     ",
    "     #    #      #    #     ",
    "     #.## #      # ##.#     ",
    "     #.## ######## ##.#     ",
    "     #.##          ##.#     ",
    "     #.## ######## ##.#     ",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#*..##.......  .......##..*#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
    ]
    for row in range(board_height):
        board.append([])
        for col in range(board_width):
            if layout[row][col] == "#":
                board[row].append("1")   #wall
            elif layout[row][col] == ".":    
                board[row].append("2")   #regular pellet
            elif layout[row][col] == "*":
                board[row].append("3")  #Powerup
            else:
                board[row].append("0")  #empty cell

    return board                         



def draw_board(surface, board):
    for row in range(board_height):
        for col in range(board_width):
            x=col*cell_size
            y=row*cell_size
            cell_value=board[row][col]
            

            if cell_value=="1":
                pygame.draw.rect(surface, BLUE, (x,y,cell_size,cell_size))   #Drawing BLUE walls


            elif cell_value=="2":
                center_x=x+cell_size//2
                center_y=y+cell_size//2
                radius=cell_size//6
                pygame.draw.circle(surface,RED,(center_x,center_y),radius)    #Drawing RED regular points  



            elif cell_value=="3":
                center_x=x+cell_size//2
                center_y=y+cell_size//2
                radius=cell_size//4
                pygame.draw.circle(surface,WHITE,(center_x,center_y),radius)  #Drawing WHITE Powerups

            



__all__ = ['create_board', 'draw_board']