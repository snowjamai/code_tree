N, M, r, c = map(int, input().split())

board = [[0] * N for _ in range(N)]

command = list(map(str, input().split()))

  
dx, dy = [1, -1, 0, 0 ], [0,0,1, -1]


row = [1, 4, 6, 3]
col = [1,5,6,2]
col_b = 2
row_b = 2
board[c- 1][r - 1] = 6
def dice(x, y, d):
    global row, col 
    

    if d == 'U':
        nx, ny = x + dx[3], y + dy[3] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return x, y, -1
        else:
            col = col[-1:] + col[:-1]
            row[0] = col[0]
            row[row_b] = col[col_b] 
            return nx, ny, row[row_b] 

    elif d == 'D':
        nx, ny = x + dx[2], y + dy[2] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return x, y,  -1
        else:
            col = col[1:] + col[:1]
            row[0] = col[0]
            row[row_b] = col[col_b] 
            return nx, ny, row[row_b] 

    elif d == 'R':
        nx, ny = x + dx[0], y + dy[0] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return x, y,  -1
        else:
            row = row[1:] + row[:1]
            col[0] = row[0]

            col[col_b] = row[row_b]
            return nx, ny, row[row_b] 

    elif d == 'L':
        nx, ny = x + dx[1], y + dy[1] 
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return x, y,  -1
        else:
            row = row[-1:] + row[:-1]
            col[0] = row[0]
            col[col_b] = row[row_b]
            return nx, ny, row[row_b] 


x, y = c - 1, r - 1 
for c in command:
    x, y, z = dice(x, y, c)
    if z != -1:
        board[y][x] = z


cnt = 0
for h in range(N):
    for w in range(N):
        cnt += board[h][w] 
print(cnt)

    