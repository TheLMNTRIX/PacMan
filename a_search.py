from collections import deque


class Node:
    def __init__(self,row,col, parent=None):
        self.row=row
        self.col=col
        self.parent=parent
        self.g=0
        self.h=0
        self.f=0
        
    
    def __eq__(self,other):
        return self.row==other.row and self.col==other.col
    
    def __hash__(self):
        return hash((self.row, self.col))
    
    def __lt__(self,other):
        return self.f<other.f
    
    
    
def manhattan_distance(node, goal_node):
    """
    Calculate the Manhattan distance between the current node and the goal node.
    """
    
    dx=abs(node.row-goal_node.row)
    dy=abs(node.col-goal_node.col)
    return dx+dy

def a_star_search(board, start_node, goal_node):
    open_list=deque([start_node])
    closed_list=set()
    
    start_node.g=0
    start_node.h=manhattan_distance(start_node,goal_node)
    start_node.f=start_node.g+start_node.h
    
    while open_list:
        current_node=open_list.popleft()
        
        if current_node==goal_node:
            path=[]
            while current_node:
                path.append(current_node)
                current_node=current_node.parent
            return path[::-1]
        
        closed_list.add(current_node)
        
        
        for neighbor in get_neighbors(board,current_node):
            if neighbor in closed_list:
                continue
            
            
            tentative_g=current_node.g+1
            
            if neighbor not in open_list:
                open_list.append(neighbor)
                
        open_list=deque(sorted(open_list))
    
    return []

def get_neighbors(board,node):
    
    neighbors=[]
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    
    for dx,dy in directions:
        neighbor_row=node.row+dx
        neighbor_col=node.col+dy
        
        if(
            0<=neighbor_row<len(board) and
            0<=neighbor_col<len(board[0]) and
            board[neighbor_row][neighbor_col]!="1"
        ):
            neighbors.append(Node(neighbor_row,neighbor_col,node))
    
    return neighbors        
