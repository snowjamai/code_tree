N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def find_num(n):
    for h in range(N):
        for w in range(N):
            if board[h][w] == n:
                return w, h 


def change(x, y, arr):
    dx , dy = [1,-1,0,0,1,1,-1,-1],[0,0,1,-1,1,-1,1,-1]
    mv = 0
    mx, my = -1, -1
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue 
        else:
            if board[ny][nx] > mv:
                mv = board[ny][nx]
                mx, my = nx, ny
    tmp = arr[y][x] 
    arr[y][x] = arr[my][mx]
    arr[my][mx] = tmp 
    return arr 

for i in range(M):
    for j in range(1, N * N + 1):
        x, y = find_num(j)
        board = change(x,y, board) 

for h in range(N):
    for w in range(N):
        print(board[h][w], end = ' ')
    print("")