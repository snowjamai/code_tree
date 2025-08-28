N = int(input())
r1, c1, r2, c2 = map(int, input().split())


sx, sy = c1 - 1, r1 - 1
ex, ey = c2 - 1, r2 - 1

dx, dy = [2, 2, 1, 1, -1,-1, -2, -2], [1, -1, 2, -2, 2,-2,1,-1]
from collections import deque 

q = deque()
visited = [[0] * N for _ in range(N)]
q.append((sx, sy))
visited[sy][sx] = 0 

def bfs(q):
    global visited
    while len(q) != 0:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            else:
                if visited[ny][nx] == 0 or visited[ny][nx] > (visited[y][x] + 1):
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))


bfs(q)
if visited[ey][ex] != 0
    print(visited[ey][ex])
else:
    print(-1)