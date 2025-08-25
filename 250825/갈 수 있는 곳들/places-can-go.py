
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




N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
q = queue() 
visited = [[0] * N for _ in range(N)]

for i in range(K):
    r, c = map(int, input().split())
    q.push((c- 1, r - 1))
    visited[r - 1][c - 1] = 1


    

def bfs(q):
    cnt = 0
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    while q.empty() == False:
        x, y = q.pop()
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if board[ny][nx] == 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1 
                q.push((nx, ny))
    return cnt 
re = bfs(q)

print(re)
        


