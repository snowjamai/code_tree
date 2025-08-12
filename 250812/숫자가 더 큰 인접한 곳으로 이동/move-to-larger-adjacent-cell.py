
dx, dy = [0,0,-1,1],[-1,1,0,0]
N, r , c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def can_move(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny >= N or nx >= N or ny < 0:
            continue 
        if board[y][x] < board[ny][nx]:
            return True 
    return False 

x, y = c - 1, r  - 1
print(board[y][x], end=' ')
while can_move(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny >= N or nx >= N or ny < 0:
            continue 
        if board[y][x] < board[ny][nx]:
            x, y= nx, ny
            print(board[y][x], end = ' ') 
            break 
        
    