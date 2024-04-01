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
        self.initial_direction=["right","left"]
        self.direction = random.choice(["up", "down", "left", "right"])
        self.color = color
        self.scatter_target = (board_width-1, board_height-1)
        self.left_center = False



    def draw(self, surface,cell_size):
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

    def update(self):
        if self.get_next_cell_value() == "1":  # Hit a wall
            self.direction = self.new_direction()

        if self.direction == "up":
            self.y -= 1
        elif self.direction == "down":
            self.y += 1
        elif self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

        if self.left_center and self.x == centrex and self.y == centrey:
            self.board[self.y][self.x]=="1"
            possible_directions = self.get_valid_directions()
            if possible_directions:
                self.direction = random.choice(possible_directions)


    def get_next_cell_value(self):
        next_x = self.x
        next_y = self.y
        if self.direction == "up":
            next_y -= 1
        elif self.direction == "down":
            next_y += 1
        elif self.direction == "left":
            next_x -= 1
        elif self.direction == "right":
            next_x += 1
        return self.board[next_y][next_x]

    def new_direction(self):
        possible_directions = self.get_valid_directions()
        if not self.left_center:
            possible_directions=random.choice(self.initial_direction)
            self.left_center=True
            return possible_directions
        if self.direction in possible_directions:
            possible_directions.remove(self.direction)
        return random.choice(possible_directions)
    def get_valid_directions(self):
        valid_directions = []
        if self.board[self.y - 1][self.x] == "0" or self.board[self.y - 1][self.x] == "2" or self.board[self.y - 1][self.x] == "3" or self.board[self.y - 1][self.x] == "4":  # Check up
            valid_directions.append("up")
        if self.board[self.y + 1][self.x] == "0" or self.board[self.y + 1][self.x] == "2" or self.board[self.y + 1][self.x] == "3" or self.board[self.y + 1][self.x] == "4" :  # Check down
            valid_directions.append("down")
        if self.board[self.y][self.x - 1] == "0" or self.board[self.y][self.x - 1] == "2" or self.board[self.y][self.x - 1] == "3" or self.board[self.y][self.x - 1] == "4":  # Check left
            valid_directions.append("left")
        if self.board[self.y][self.x + 1] == "0" or self.board[self.y][self.x + 1] == "2" or self.board[self.y][self.x + 1] == "3" or self.board[self.y][self.x + 1] == "4":  # Check right
            valid_directions.append("right")


        return valid_directions








