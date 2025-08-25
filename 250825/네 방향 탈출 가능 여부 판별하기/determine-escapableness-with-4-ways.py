from collections import deque 

class queue:
    def __init__(self):
        self.q = deque() 
    
    def empty(self):
        if len(self.q) == 0:
            return True 
        else:
            return False 
    def push(self,v):
        self.q.append(v)
    def pop(self):
        return self.q.popleft()
    def front(self):
        return self.q[0]


N, M = map(int, input().split())

q = queue() 


board = [list(map(int, input().split())) for _ in range(N)]


def bfs(q):
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1 

    q.push((0,0))
    suc = 0
    dx , dy = [1,-1, 0,0], [0,0,1,-1]

    while q.empty() == False:
        a = q.pop()
        x, y = a[0], a[1] 
        if x == (M - 1) and y == (N - 1):
            suc = 1 
            break 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue 
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = 1 
                q.push((nx, ny))
    return suc

result = bfs(q)

print(result)


        