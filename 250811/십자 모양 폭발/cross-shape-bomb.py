def bomb(x, y):
    bomb_size = board[y][x]
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    # print(bomb_size, x, y)
    for i in range(bomb_size):
        for j in range(4):
            nx, ny = x + dx[j] * i, y +dy[j] * i
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            else:
                board[ny][nx] = -1 
            
def make_down(x, y):
    while board[y][x] == -1:
        for i in range(y, 0,-1):
            board[i][x] = board[i - 1][x]
        board[0][x] = 0

def print_board():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print("")


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int,input().split())
bomb(c - 1, r - 1)
# print_board()


for i in range(N -1, -1, -1):
    for j in range(N):
        make_down(j, i)
print_board() 
        # print("_-------")



        

        