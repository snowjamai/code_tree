N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

import copy

def dfs(x, y, v):
    dx, dy = [1,-1,0,0],[0,0,1,-1]

    for i in range(4):
        nx, ny =  x + dx[i], y + dy[i] 
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue 
        if tmp[ny][nx] <= k:
            tmp[ny][nx] = 0 
        
        if visited[ny][nx] == 0 and tmp[ny][nx] != 0:
            visited[ny][nx] = v
            dfs(nx, ny, v)




max_v = 0
max_k = 0 

for k in range(1, 101):
    tmp = copy.deepcopy(board)
    visited = [[0] * M for _ in range(N)]
    v = 0
    for h in range(N):
        for w in range(M):
            if tmp[h][w] <= k:
                tmp[h][w] = 0
            if tmp[h][w] != 0:
                v += 1
                dfs(w, h, v)
               
    if v > max_v:
        max_v = v 
        max_k = k 
print(max_k)


            