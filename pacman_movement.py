import pygame

#PacMan initial position

pacman_start_row=22.5
pacman_start_col=13.5
YELLOW=(255,255,0)

class pacman:
    def __init__(self,board):
        self.board=board
        self.row=pacman_start_row
        self.col=pacman_start_col
        self.score=0
        self.lives=3

    def move(self, pressed_keys):
        #using move_vectors
        move_row, move_col = 0, 0
        if pressed_keys[0] or pressed_keys[1] or pressed_keys[2] or pressed_keys[3]:
            if pressed_keys[0]:
                move_row, move_col = 0, -1
            elif pressed_keys[1]:
                move_row, move_col = 0, 1
            elif pressed_keys[2]:
                move_row, move_col = -1, 0
            elif pressed_keys[3]:
                move_row, move_col = 1, 0
            else:
                move_row, move_col = 0, 0
            #calculating new position
        new_row=int(self.row+move_row)
        new_col=int(self.col+move_col)

        #check for walls
        if self.board[new_row][new_col]=="1":
            return
        
        self.row=new_row
        self.col=new_col

        #check for points
        self.handle_collisions(new_row,new_col)

    def handle_collisions(self,row,col):
        cell_value=self.board[row][col]
        if cell_value=="3":
            self.score += 10
            self.board[row][col]="0"

        elif cell_value=="2":
            self.score += 50
            self.board[row][col]="0"


    def draw(self, surface, cell_size):
        pacman_x=self.col*cell_size
        pacman_y=self.row*cell_size
        pygame.draw.circle(surface,YELLOW,(pacman_x+cell_size//2,pacman_y+cell_size),cell_size//2)            




__all__=["pacman"]