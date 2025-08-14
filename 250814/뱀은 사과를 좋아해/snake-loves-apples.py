N, M, K = map(int, input().split())
board = [[0] * N for  _ in range(N)]

apple = []
for i in range(M):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1 


# 1 은 사과 


move = []
for k in range(K):
    d, p = map(str, input().split())
    move.append((d, int(p)))

snake = [0] * 1001 
snake[0] = (0,0)
snake_head = 0 

def simul(x, y, d):
    global snake_head, snake

    if d == 'L':
        dx, dy = -1, 0 
        nx, ny = x + dx, y + dy 
        
    elif d == 'R':
        dx, dy = 1, 0 
        nx, ny = x + dx, y + dy 
    elif d == 'U':
        dx, dy = 0, -1 
        nx, ny = x + dx, y + dy 
    elif d == 'D':
        dx, dy = 0, 1 
        nx, ny = x + dx, y + dy 

    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return -1 ,nx, ny
    else:
        if board[ny][nx] == 0:
            tail = snake[0]
            board[tail[1]][tail[0]] = 0 
            snake = snake[1:] + [0]
            snake[snake_head] = (nx, ny) 
            
            board[ny][nx] = 2
            return 1, nx, ny
        elif board[ny][nx] == 1:
            snake_head += 1
            snake[snake_head] = (nx, ny)
            board[ny][nx] = 2
            return 1 ,nx,ny
        elif board[ny][nx] == 2:
            if snake[0][0] == nx and snake[0][1] == ny:
                tail = snake[0]
                board[tail[1]][tail[0]] = 0 
                snake = snake[1:] + [0]
                snake[snake_head] = (nx, ny) 
                return 1, nx, ny 
            else:
                return -1 ,nx,ny
    


def pb():
    for h in range(N):
        for w in range(N):
            print(board[h][w], end = ' ' )
        print("") 


x, y = 0 , 0
board[y][x] = 2
die = False 
die_t = 0
d= 0
for m in move:
    d, p = m[0], m[1]
    for i in range(p):
        # print(x, y, d)
        suc, x, y = simul(x, y,d)
        if suc == -1:
            die = True 
            die_t += 1
            break 
        # pb()
        die_t += 1 

    if die == True:
        break 

print(die_t)

            

