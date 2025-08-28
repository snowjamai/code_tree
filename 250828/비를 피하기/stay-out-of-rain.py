N, H, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
from collections import deque

dx, dy = [1,-1,0,0],[0,0,1,-1]
def get_min_mv(x, y):
    q = deque() 
    visited = [[-1] * N for _ in range(N)]

    q. append((x, y))
    visited[y][x] = 0

    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if (visited[ny][nx] == -1 and board[ny][nx] != 1)  or (visited[ny][nx] > ( visited[y][x] + 1) and  board[ny][nx] != 1):
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))
                if board[ny][nx] == 3:
                    return visited[ny][nx] 
    return - 1





for h in range(N):
    for w in range(N):
        if board[h][w] == 0 or board[h][w] == 1 or board[h][w] == 3:
            result[h][w] = 0 
        else:
            result[h][w] = get_min_mv(w,h)

for h in range(N):
    for w in range(N):
        print(result[h][w], end = ' ')
    print("")
