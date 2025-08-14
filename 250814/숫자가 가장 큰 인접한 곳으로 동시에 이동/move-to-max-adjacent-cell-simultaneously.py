import copy


N, M, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

ball = [[0] * N for _ in range(N)]
for i in range(M):
    r, c = map(int, input().split())
    ball[r - 1][c - 1] = 1



dx, dy = [0, 0, -1,1], [-1,1,0,0]


def pb():
    for h in range(N):
        for w in range(N):
            print(ball[h][w], end = ' ')
        print("")


def move_ball(x, y, arr):
    max_v = 0
    max_idx = -1 

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue 
        else:
            if board[ny][nx] > max_v:
                max_v = board[ny][nx] 
                max_idx = (nx, ny)
    if max_idx != -1:
        arr[max_idx[1]][max_idx[0]] += 1 
        
    return arr 
def eliminate(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2:
                arr[i][j] = 0
    return arr 

for i in range(T):
    tmp = [[0] * N for _ in range(N)]

    for h in range(N):
        for w in range(N):
            if ball[h][w] == 1:
                tmp = move_ball(w, h, tmp)

    ball = copy.deepcopy(tmp)
    # pb() 
    # print("------")
    ball = eliminate(ball)
    # pb() 
    # print("------")
cnt = 0 

for h in range(N):
    for w in range(N):
        if ball[h][w] != 0:
            cnt += ball[h][w]

print(cnt)