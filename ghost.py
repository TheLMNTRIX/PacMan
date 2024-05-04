import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

board_width = 28
board_height = 31
cell_size = 24


centrex = board_width // 2 * cell_size
centrey = board_height // 2 * cell_size


class Ghost:
    def __init__(self, board, start_x, start_y, color):
        self.centrex = board_width // 2 * cell_size
        self.centrey = board_height // 2 * cell_size
        self.x = start_x
        self.y = start_y
        self.board = board
        self.color = color
        self.scatter_target = (board_width - 1, board_height - 1)
        self.left_center = False

    def draw(self, surface, cell_size):
        center_x = self.x * cell_size + cell_size // 2
        center_y = self.y * cell_size + cell_size // 2
        radius = cell_size // 2

        # Main body of the ghost
        pygame.draw.circle(surface, self.color, (center_x, center_y), radius)

        # Eyes
        eye_radius = radius // 5
        eye_offset = radius // 3
        left_eye_center = (center_x - eye_offset, center_y - eye_offset)
        right_eye_center = (center_x + eye_offset, center_y - eye_offset)

        pygame.draw.circle(surface, WHITE, left_eye_center, eye_radius)
        pygame.draw.circle(surface, WHITE, right_eye_center, eye_radius)
        pygame.draw.circle(surface, BLACK, left_eye_center, eye_radius // 2)
        pygame.draw.circle(surface, BLACK, right_eye_center, eye_radius // 2)
        pygame.draw.rect(surface, self.color, (center_x - radius, center_y, radius * 2, radius))

    # The update method is no longer needed since the ghost movement is now handled by the A* algorithm in main.py