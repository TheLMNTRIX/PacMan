import pygame
import random
from game_board import create_board, draw_board, window_width, window_height, BLACK, cell_size
from pacman_movement import pacman



def main():
    pygame.init()
    window=pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption("PacMan")
    clock=pygame.time.Clock()

    board=create_board()
    pacman_instance = pacman(board)   #creating pacman object

    running=True

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            elif event.type==pygame.KEYDOWN:   #move event
                    pacman_instance.move(event)      


        window.fill(BLACK)
        draw_board(window,board)
        pacman_instance.draw(window, cell_size)  
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()