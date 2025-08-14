N, M, K = map(int, input().split())
board = [[0] * N for  _ in range(N)]

apple = []
for i in range(M):
    x, y = map(int, input().split())
    board[y - 1][x - 1] = 1 


# 1 은 사과 


move = []
for k in range(K):
    d, p = map(str, input().split())
    move.append((d, int(p)))

snake = [0] * 1001 
snake[0] = (4,0)
snake_head = 0 

def simul(x, y, d):
    global snake_head, snake

    if d == 'L':
        dx, dy = -1, 0 
        nx, ny = x + dx, y + dy 
        if nx < 0 or ny < 0 or nx >= N or nx >= N:
            return -1 ,nx,ny
        else:
            print(nx, ny)
            if board[ny][nx] == 0:
                tail = snake[0]
                print(tail)
                board[tail[1]][tail[0]] = 0 
                snake = snake[1:]
                snake[snake_head] = (nx, ny) 
                board[ny][ny] = 2
                return 1, nx, ny
            elif board[ny][nx] == 1:
                snake_head += 1
                snake[snake_head] = board[ny][nx]
                board[ny][nx] = 2
                return 1 ,nx,ny
            elif board[ny][nx] == 2:
                return -1 ,nx,ny


def pb():
    for h in range(N):
        for w in range(N):
            print(board[h][w], end = ' ' )
        print("") 

pb()
x, y = 4 , 0
die = False 
die_t = 0
for m in move:
    d, p = m[0], m[1]
    for i in range(p):
        print(x, y, d)
        suc, x, y = simul(x, y,d)
        print(suc)
        if suc == -1:
            die = True 
            break 
        pb()
        die_t += 1 
    if die == True:
        break 
print(die_t)

            

