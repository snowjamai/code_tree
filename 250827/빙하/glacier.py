N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

q = deque()
for n in range(N):
    for m in range(M):
        if board[n][m] == 1:
            q.append((m,n))

dx, dy = [1,-1,0,0], [0,0,1,-1]

def make_eli_water():
    water = deque() 
    water.append((0,0))
    
    while len(water) != 0:
        x, y = water.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue 
            if board[ny][nx] == 0:
                board[ny][nx] = -1
                water.append((nx, ny))

def can_eliminate(x, y):
    for i in range(4):
        nx , ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue 
        if board[ny][nx] == -1:
            return True
    return False

ice = deque() 

for h in range(N):
    for w in range(M):
        if board[h][w] == 1:
            ice.append((w, h))

make_eli_water()
t = 0
import copy 

def spread(x, y , arr):
    q = deque()
    q.append((x, y))
    
    while len(q) != 0:
        x, y = q.popleft() 
        for i in range(4):
            nx ,ny = x + dx[i], y + dy[i] 
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue 
            if arr[ny][nx] == 0:
                arr[ny][nx] = -1
                q.append((nx, ny))
    return arr 
            

while len(ice) != 0:
    t += 1
    tmp_board = copy.deepcopy(board)
    tmp = deque() 
    ice_melt = 0

    while len(ice) != 0:
        ix, iy = ice.popleft()
        if can_eliminate(ix,iy) == False:
            tmp.append((ix, iy))
        else:
            ice_melt += 1
            tmp_board[iy][ix] = -1 
            tmp_board = spread(ix, iy, tmp_board)

    board = tmp_board
    ice = tmp 



    


print(t, ice_melt)
    