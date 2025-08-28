from collections import deque

dx, dy = [1,-1,0,0], [0,0,1,-1]

N, K, U, D = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dx , dy = [1, -1, 0,0 ], [0,0, 1, -1]
import copy 

def dfs(que):
    q = copy.deepcopy(que)
    visited = [[0] * N for _ in range(N)]   
    cnt = 0

    while len(q) != 0:
        x, y = q.popleft() 
        visited[y][x] = 1
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if visited[ny][nx] == 0 and abs(board[y][x] - board[ny][nx]) >= U and abs(board[y][x] - board[ny][nx])<= D:
                visited[ny][nx] = 1
                q.append((nx, ny))

    return cnt 

max_n = 0
def select(l, idx):
    global max_n
    if len(l) == K:
        n = dfs(l)
        if max_n < n:
            max_n = n 
        return 
    else:
        for i in range(idx, N * N):
            l.append((i % N, i // N))
            select(l, i + 1)
            l.pop()

city = deque() 

select(city, 0)
print(max_n)