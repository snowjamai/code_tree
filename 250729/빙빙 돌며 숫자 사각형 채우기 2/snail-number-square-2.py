N, M = map(int, input().split())

# Please write your code here.

dx, dy = [0,1,0,-1], [1,0,-1,0]

cx,cy = 0, 0
d = 0

board = [[0]*M for _ in range(N)]

for i in range(1, N * M + 1):
    # print(cx, cy)
    board[cy][cx] = i

    nx, ny = cx + dx[d], cy + dy[d] 

    if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] != 0:
        d = (d + 1) % 4 
        nx, ny = cx + dx[d], cy + dy[d] 

    cx, cy = nx, ny 

for h in range(N):
    for w in range(M):
        print(board[h][w], end=' ')
    print("")

    