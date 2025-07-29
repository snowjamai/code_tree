N, M = map(int, input().split())

# Please write your code here.
chr(65)


d = 0 

dx, dy = [1,0,-1,0],[0,1,0,-1]

cx,cy = 0, 0

board = [[0] * M for _ in range(N)]

for i in range(N * M ):

    board[cy][cx] = chr((i%26 + 65 ))
    nx, ny = cx + dx[d], cy + dy[d]

    if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] != 0:
        d = (d + 1) % 4 
        nx, ny = cx + dx[d] , cy + dy[d]

    cx, cy = nx, ny 

for h in range(N):
    for w in range(M):
        print(board[h][w], end=' ')
    print("")