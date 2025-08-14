N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]


dx, dy = [1,0,-1,0], [0,1,0,-1]

def simul(x, y, d):
    t = 1
    while True: 
        nx, ny = x + dx[d], y + dy[d] 
        t += 1 

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            return t
        else:
            if board[ny][nx] == 0:
                x, y = nx, ny
            elif board[ny][nx] == 1:
                if d == 0:
                    d = 3 
                elif d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 0 
                # nx, ny = x, y 
                x, y = nx, ny
                
            elif board[ny][nx] == 2:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d== 3:
                    d = 2 
                # nx, ny = x, y 
                x, y = nx, ny
                
max_t = 0
for i in range(N):
    t = simul(i, 0, 1)
    if t > max_t:
        max_t = t 
for i in range(N):
    t = simul(N - 1, i, 2)
    if t > max_t:
        max_t = t 

for i in range(N):
    t = simul(i, N - 1, 3)
    if t > max_t:
        max_t = t 

for i in range(N):
    t = simul(0, i, 0)
    if t > max_t:
        max_t = t 

print(max_t)