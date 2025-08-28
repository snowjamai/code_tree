import copy
from collections import deque 

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

sx, sy = c1 - 1, r1 - 1
ex, ey = c2 - 1, r2 - 1 

wall = []
for h in range(N):
    for w in range(N):
        if board[h][w] == 1:
            wall.append((w, h))

W = len(wall)
def del_wall(l):
    tmp = copy.deepcopy(board) 
    for i in l:
        tmp[i[1]][i[0]] = 0 

    return tmp 
dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(arr):
    visited = [[-1] * N for _ in range(N)]
    q= deque()
    q.append((sx, sy))
    visited[sy][sx] = 0 

    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if visited[ny][nx] == -1 and arr[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1 
                q.append((nx, ny))

    return visited[ey][ex]



min_t = N * N
do = False
def wall_select(l, idx):
    global min_t, do
    if len(l) == K:
        tmp_board = del_wall(l)
        t = bfs(tmp_board)
        if t == -1:
            return
        else:
            if min_t > t:
     
                do = True 
         
                min_t = t
            return
    for i in range(idx, W):
        l.append( (wall[i][0], wall[i][1]))
        wall_select(l, idx + 1)
        l.pop()

wall_select([], 0)

if do == True:
    print(min_t)
else:
    print(-1)