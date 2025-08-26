N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

r, c = map(int, input().split())

sx, sy = c-1, r - 1

from collections import deque

class queue:
    def __init__(self):
        self.q = deque()

    def empty(self):
        if len(self.q) == 0:
            return True 
        else:
            return False 

    def push(self, v):
        self.q.append(v)

    def pop(self):
        return self.q.popleft()
    def front(self):
        return self.q[0]

q = queue() 
q.push((sx, sy))

def bfs(q, base_x, base_y):
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    visited = [[0] * N for _ in range(N)]
    visited[base_y][base_x] = 1
    max_x, max_y = N - 1, N - 1
    max_v = 0
    while q.empty() == False:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if board[base_y][base_x] > board[ny][nx] and visited[ny][nx] == 0:
                if max_v < board[ny][nx]:
                    max_v = board[ny][nx]
                    max_x, max_y = nx, ny
                    visited[ny][nx] = 1
                    q.push((nx, ny))

                elif max_v == board[ny][nx]:
                    if max_y > ny:
                        max_y = ny 
                        max_x = nx 
                        visited[ny][nx] = 1
                        q.push((nx, ny))
                    elif max_y == ny:
                        if max_x > nx:
                            max_x = nx 
                            max_y = ny 
                            visited[ny][nx] = 1
                            q.push((nx, ny))
                    else:
                        visited[ny][nx] = 1
                        q.push((nx, ny))
                else:
                    visited[ny][nx] = 1
                    q.push((nx, ny))


                    

    return max_x, max_y

for k in range(K):
    a, b = bfs(q,sx, sy)
    sx, sy = a, b
    q.push((sx, sy))
print(b + 1, a + 1)