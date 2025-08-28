from collections import deque 

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

visited = [[0] * M for _ in range(N)]
def bfs(q):
    global visited
    x, y = q[0]

    visited[y][x] = 1 
    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue 
            if visited[ny][nx] == 0 and board[ny][nx] == 1 or (visited[ny][nx] > (visited[y][x] + 1) and board[ny][nx] == 1):
                visited[ny][nx] = visited[y][x] + 1 
                q.append((nx, ny))
        

q = deque() 
q.append((0, 0))


bfs(q)
print(visited[M - 1][N - 1] - 1)


