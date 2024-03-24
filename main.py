import pygame
import random
from game_board import create_board, draw_board, window_width, window_height, BLACK



def main():
    pygame.init()
    window=pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption("PacMan")
    clock=pygame.time.Clock()

    board=create_board()

    running=True

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False


        window.fill(BLACK)
        draw_board(window,board)
        pygame.display.flip()


    pygame.quit()


if __name__ == "__main__":
    main()