import pygame

#PacMan initial position

pacman_start_row=22.5
pacman_start_col=13.5
YELLOW=(255,255,0)
#movement vectors
move_vectors={
    pygame.K_LEFT:(0,-1),
    pygame.K_RIGHT:(0,1),
    pygame.K_UP:(-1,0),
    pygame.K_DOWN:(1,0)
}


class pacman:
    def __init__(self,board):
        self.board=board
        self.row=pacman_start_row
        self.col=pacman_start_col
        self.score=0
        self.lives=3

    def move(self,event):
        #using move_vectors
        if event.type==pygame.KEYDOWN:
            direction=move_vectors.get(event.key,None)

        if direction:
            move_row, move_col= direction    

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