from collections import deque 


N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

rotten = deque()
visited = [[-1] * N for _ in range(N)]

for h in range(N):
    for w in range(N):
        if board[h][w] == 2:
            rotten.append((w, h))
            visited[h][w] = 0

def bfs(q):
    dx, dy = [1,-1,0,0], [0, 0, 1, -1]
    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if board[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1 
                q.append((nx, ny))


bfs(rotten)
for h in range(N):
    for w in range(N):
        if visited[h][w] == -1 and board[h][w] == 1:
            print(-2, end = ' ')
        else:
            print(visited[h][w], end = ' ')
    print("")