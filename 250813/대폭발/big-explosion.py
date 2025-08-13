import copy 

N, M , r, c = map(int, input().split())

board = [[0] * N for _ in range(N)]
def pb():
    for h in range(N):
        for w in range(N):
            print(board[h][w], end = ' ')
        print("")
def simul(x, y, t, arr):
    length = 2 ** (t - 1) 
    dx, dy = [1,-1,0,0],[0,0,1,-1]
    arr[y][x] = 1 
    
    for j in range(4):
        nx, ny = x + dx[j] * length , y + dy[j] * length
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue 
        else:

            arr[ny][nx] = 1 

    return arr 

board[r - 1][c- 1] = 1 

for t in range(1, M + 1):
    tmp = copy.deepcopy(board)
    for h in range(N):
        for w in range(N):
            if board[h][w] == 1:
                tmp = simul(w, h, t, tmp)
    board = copy.deepcopy(tmp)

    # print(tmp)

cnt = 0 
for h in range(N):
    for w in range(N):
        if board[h][w] == 1:
            cnt += 1

print(cnt)


    
