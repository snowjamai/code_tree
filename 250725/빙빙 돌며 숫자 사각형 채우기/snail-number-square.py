N, M = map(int, input().split())

dx, dy = [1,0,-1,0],[0,1,0, -1]

num = 1

visit = [[0]*M for _ in range(N)]
board = [[0]*M for _ in range(N)]

cx, cy = 0 , 0 
d = 0


board[cy][cx] = num

for i in range(1, N*M ):
    nx, ny = cx + dx[d], cy + dy[d] 
    if nx < 0 or nx >= M or ny < 0 or ny >= N or board[ny][nx] != 0:
        d = (d + 1) % 4 
        nx, ny = cx + dx[d], cy + dy[d] 
    
    board[ny][nx] = num + 1
    num += 1
    cx, cy = nx, ny
   

for i in range(N):
    for j in range(M):
        print(board[i][j], end=' ')
    print("")
