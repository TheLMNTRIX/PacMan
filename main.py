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
    pressed_keys = [False, False, False, False]
    running=True

    while running:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pressed_keys[0] = True
                elif event.key == pygame.K_RIGHT:
                    pressed_keys[1] = True
                elif event.key == pygame.K_UP:
                    pressed_keys[2] = True
                elif event.key == pygame.K_DOWN:
                    pressed_keys[3] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressed_keys[0] = False
                elif event.key == pygame.K_RIGHT:
                    pressed_keys[1] = False
                elif event.key == pygame.K_UP:
                    pressed_keys[2] = False
                elif event.key == pygame.K_DOWN:
                    pressed_keys[3] = False

        pacman_instance.move(pressed_keys)   #move pacman

        window.fill(BLACK)       #drawing the board
        draw_board(window,board)
        pacman_instance.draw(window, cell_size)  
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()