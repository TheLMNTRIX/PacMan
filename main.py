import pygame
import random
from game_board import create_board, draw_board, window_width, window_height, BLACK, cell_size, WHITE
from pacman_movement import pacman
from ghost import Ghost
from a_search import a_star_search, Node

GREEN = (50, 205, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
board_width = 28
board_height = 31

def main():
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("PacMan")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)
    board = create_board()
    pacman_instance = pacman(board)
    ghost_start_x_white = 14
    ghost_start_y_white = 11
    ghost_start_x_red = 14
    ghost_start_y_red = 13
    ghost_start_x_green = 14
    ghost_start_y_green = 16
    ghost1 = Ghost(board, ghost_start_y_red, ghost_start_x_red, RED)
    ghost2 = Ghost(board, ghost_start_y_green, ghost_start_x_green, GREEN)
    ghost3 = Ghost(board, ghost_start_y_white, ghost_start_x_white, WHITE)
    ghosts = [ghost1, ghost2, ghost3]
    pressed_keys = [False, False, False, False]
    running = True

    while running:
        clock.tick(8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

        pacman_instance.move(pressed_keys)  # Move Pacman

        # Move ghosts using A* algorithm
        for ghost in ghosts:
            start_node = Node(ghost.y, ghost.x)
            goal_node = Node(pacman_instance.row, pacman_instance.col)  # Pacman's position as the goal
            path = a_star_search(board, start_node, goal_node)
            if path:
                next_node = path[1]  # Get the next node in the path
                ghost.y = next_node.row
                ghost.x = next_node.col

        window.fill(BLACK)
        draw_board(window, board)
        pacman_instance.draw(window, cell_size)
        for ghost in ghosts:
            ghost.draw(window, cell_size)
        text = font.render("Score: " + str(pacman_instance.score), True, WHITE)
        window.blit(text, (10, window_height - 30))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()