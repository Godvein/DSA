import os
import time
maze = [[0,1,1,1,1,1,1],
        [0,0,1,1,1,1,1],
        [1,0,0,0,0,1,1],
        [1,1,0,1,0,1,1],
        [1,1,1,1,0,0,0]]

rows = len(maze)
cols = len(maze[0])


visited = [[False] * cols for _ in range(rows)]

def clear_console():
    
    os.system('cls' if os.name == 'nt' else 'clear')


def print_maze(maze):
    clear_console()
    for row in maze:
        print(" ".join(str(cell) for cell in row))
    print()  

def dfs_traversal(r,c):
    if c < 0 or c >= cols or r < 0 or r >= rows or visited[r][c] or maze[r][c] == 1:
        return
    visited[r][c] = True
    maze[r][c] = "*"
    print_maze(maze)
    time.sleep(0.5)
    dfs_traversal(r+1,c)
    dfs_traversal(r-1,c)
    dfs_traversal(r,c+1)
    dfs_traversal(r,c-1)

dfs_traversal(0,0)